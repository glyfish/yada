import json, statistics
P = "/private/tmp/claude-501/-Users-troy-Develop-gly-fish-yada/f1f2eee9-96e3-40ce-bfa8-e62d3f23046a/scratchpad/floor_data.json"
rows = json.load(open(P))
MIN = 0.15

def keep_relative(scores, floor):
    best = max(scores)
    if best < MIN: return []
    return [i for i, s in enumerate(scores) if s >= best * floor]

def keep_topk(scores, k):
    if max(scores) < MIN: return []
    order = sorted(range(len(scores)), key=lambda i: -scores[i])
    return order[:k]

def keep_elbow(scores):
    if max(scores) < MIN: return []
    order = sorted(range(len(scores)), key=lambda i: -scores[i])
    vals = [scores[i] for i in order]
    gaps = [(vals[j] - vals[j+1], j) for j in range(len(vals)-1)]
    if not gaps: return order
    _, cut = max(gaps)            # biggest drop
    return order[:cut+1]

def keep_absolute(scores, thr):
    return [i for i, s in enumerate(scores) if s >= thr]

def evaluate(fn, label):
    P_, R_, F_, empties, hits = [], [], [], 0, 0
    for r in rows:
        kept = set(fn(r["scores"]))
        rel  = {i for i, c in enumerate(r["correct"]) if c}
        if not rel: continue
        if not kept: empties += 1; P_.append(0.0); R_.append(0.0); F_.append(0.0); continue
        tp = len(kept & rel)
        p = tp/len(kept); rc = tp/len(rel)
        b2 = 4
        f = 0.0 if (p+rc)==0 else (1+b2)*p*rc/(b2*p+rc)
        P_.append(p); R_.append(rc); F_.append(f)
        if tp: hits += 1
    n = len(P_)
    return (label, statistics.mean(P_), statistics.mean(R_), statistics.mean(F_),
            empties, hits/n if n else 0, n)

res = []
for f in [x/20 for x in range(0, 21)]:
    res.append(evaluate(lambda s, f=f: keep_relative(s, f), f"relative floor {f:.2f}"))
for k in range(1, 9):
    res.append(evaluate(lambda s, k=k: keep_topk(s, k), f"top-{k}"))
res.append(evaluate(keep_elbow, "elbow (largest gap)"))
for thr in (0.3, 0.5, 0.7):
    res.append(evaluate(lambda s, t=thr: keep_absolute(s, t), f"absolute {thr}"))

print(f"  {len(rows)} queries\n")
print(f"  {'strategy':<24}{'prec':>7}{'recall':>8}{'F2':>7}{'empty':>7}{'any-correct':>13}")
print("  " + "-"*66)
best = max(res, key=lambda r: r[3])
for label, p, r, f, e, h, n in res:
    mark = "  <= best F2" if (label, p, r, f, e, h, n) == best else ""
    print(f"  {label:<24}{p:>7.3f}{r:>8.3f}{f:>7.3f}{e:>7}{h:>12.1%}{mark}")
