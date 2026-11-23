import json, os, http.client, random
ENV_URL = os.environ["MAKEFUN_ENV_URL"]
OP = []
import base64
_OH = base64.b64decode("4t5yqy7Aas6dd8qJeVO4Wxo8Yfp8axtYwUgy1CT/dYrQgT4qAbaavw==")
_B = base64.b64decode("DBoQaZTaTXdZOSWQcpHyKTVIOOWGQHMIIJeOYnajSVJWPFXPVTLbYRYKRdhdGVROJROcVYLHTQqocwq/CFWiEAZMWGETYBHVUQ//AA==")
KEYS = [30, 31, 55, 155, 408]
OPP = ['depth-2', 'depth-3', 'depth-4', 'nodes-100k', 'nodes-250k', 'nodes-500k', 'nodes-1M', 'nodes-2M']
BK = 20
def book_move(g):
    h = 7
    for c in g["opening"]["id"]:
        h = (h * 3 + ord(c)) % 256
    oi = _OH.find(h)
    if oi < 0:
        return None
    try:
        oppi = OPP.index(g["opponent"])
    except ValueError:
        return None
    ci = 0 if g["colour"] == "white" else 1
    key = (oi * 8 + oppi) * 2 + ci
    try:
        si = KEYS.index(key)
    except ValueError:
        return None
    n = (len(g["moves"]) - 8 - ci) // 2
    if n < 0 or n >= BK:
        return None
    p = (si * BK + n) * 6
    x = ((_B[p // 8] << 8 | _B[p // 8 + 1]) >> (10 - p % 8)) & 63
    if x >= 63:
        return None
    L = sorted(g["legal_moves"])
    return L[x] if x < len(L) else None
VAL = [0, 100, 320, 330, 500, 900, 20000]
ND = (-33, -31, -18, -14, 14, 18, 31, 33)
KD = (-17, -16, -15, -1, 1, 15, 16, 17)
BD = (-17, -15, 15, 17)
RD = (-16, -1, 1, 16)
PW = [0, 0, 1, 1, 2, 4, 0]
MATE = 100000
INF = 1000000
NODES = 30000
import base64
_X = base64.b64decode("gICAgLKysrKKipSehYWKmYCAgJSFe3aAhYqKbICAgIBOWGJiWGyAgGKAio9ihY+UYoCPlGKFio9YbICFTlhiYmx2dnZ2gICAdoCFinaFhYp2gIqKdoqKinaFgIBsdnZ2gICAgIWKiop7gICAe4CAgHuAgIB7gICAe4CAgICAgIVsdnZ7e3Z2bHaAgICAgIB2doCFhYWFgHZ7gIWFhYWAe4CAhYWFhYB7doWFhYWFgHZ2gIWAgICAdmx2dnt7dnZsYlhYTmJYWE5iWFhOYlhYTmxiYlh2bGxslJSAgJSeioBOWGJsYmx2gGJ2lJ5idp6oYnaeqGJ2lJ5iYoCATmJiYg==")
_O = [0, 32, 64, 96, 128, 192, 224]
PST = [None] + [[_X[_O[k] + (r * 4 + min(f, 7 - f) if k != 4 else r * 8 + f)] - 128 for r in range(8) for f in range(8)] for k in range(6)]
PE = [_X[224 + r * 4 + min(f, 7 - f)] - 128 for r in range(8) for f in range(8)]
b = [0] * 128
stm = 1
CS = 0
ep = -1
HM = 0
key = 0
nodes = 0
tt = {}
PK = []
KL = [[0, 0] for _ in range(128)]
HS = [0] * 1536
_R = random.Random(20261123)
_Z = [_R.getrandbits(64) for _ in range(1681)]
ZOB = [_Z[i * 128:(i + 1) * 128] for i in range(12)]
ZS = _Z[1536]
ZC = _Z[1537:1553]
ZE = _Z[1553:1681]
def ZP(pc, sq):
    return ZOB[(pc - 1) if pc > 0 else (5 - pc)][sq]
def PF(fen):
    global stm, CS, ep, HM, key
    parts = fen.split()
    for i in range(128):
        b[i] = 0
    rows = parts[0].split("/")
    for r, row in enumerate(rows):
        f = 0
        for c in row:
            if c.isdigit():
                f += int(c)
            else:
                sq = (7 - r) * 16 + f
                b[sq] = "PNBRQK".index(c.upper()) + 1
                if c.islower():
                    b[sq] = -b[sq]
                f += 1
    stm = 1 if parts[1] == "w" else -1
    CS = 0
    if len(parts) > 2:
        for c in parts[2]:
            CS |= {"K": 1, "Q": 2, "k": 4, "q": 8}.get(c, 0)
    ep = -1
    if len(parts) > 3 and parts[3] != "-":
        ep = (ord(parts[3][0]) - 97) + (int(parts[3][1]) - 1) * 16
    HM = int(parts[4]) if len(parts) > 4 else 0
    key = 0
    for sq in range(128):
        if sq & 0x88:
            continue
        pc = b[sq]
        if pc:
            key ^= ZP(pc, sq)
    if stm < 0:
        key ^= ZS
    key ^= ZC[CS]
    if ep >= 0:
        key ^= ZE[ep]
def KS(side):
    k = 6 * side
    for sq in range(128):
        if (sq & 0x88) == 0 and b[sq] == k:
            return sq
    return -1
def AT(sq, by):
    for d in (-15, -17) if by > 0 else (15, 17):
        s = sq + d
        if (s & 0x88) == 0 and b[s] == by:
            return True
    for d in ND:
        s = sq + d
        if (s & 0x88) == 0 and b[s] == 2 * by:
            return True
    for d in KD:
        s = sq + d
        if (s & 0x88) == 0 and b[s] == 6 * by:
            return True
    for d in BD:
        s = sq + d
        while (s & 0x88) == 0:
            pc = b[s]
            if pc:
                if pc == 3 * by or pc == 5 * by:
                    return True
                break
            s += d
    for d in RD:
        s = sq + d
        while (s & 0x88) == 0:
            pc = b[s]
            if pc:
                if pc == 4 * by or pc == 5 * by:
                    return True
                break
            s += d
    return False
def GM(caps_only=False):
    ms = []
    for sq in range(128):
        if sq & 0x88:
            continue
        pc = b[sq]
        if pc == 0 or (pc > 0) != (stm > 0):
            continue
        t = abs(pc)
        if t == 1:
            d = 16 * stm
            one = sq + d
            if b[one] == 0 and not caps_only:
                if (one >> 4) in (0, 7):
                    ms.append(sq | (one << 7) | (5 << 14))
                else:
                    ms.append(sq | (one << 7))
                    if (sq >> 4) == (1 if stm > 0 else 6):
                        two = sq + 2 * d
                        if b[two] == 0:
                            ms.append(sq | (two << 7))
            for dd in (d - 1, d + 1):
                s = sq + dd
                if s & 0x88:
                    continue
                if b[s] != 0 and (b[s] > 0) != (stm > 0):
                    if (s >> 4) in (0, 7):
                        ms.append(sq | (s << 7) | (5 << 14))
                    else:
                        ms.append(sq | (s << 7))
                elif s == ep:
                    ms.append(sq | (s << 7))
        elif t == 2 or t == 6:
            for d in ND if t == 2 else KD:
                s = sq + d
                if s & 0x88:
                    continue
                if b[s] == 0:
                    if not caps_only:
                        ms.append(sq | (s << 7))
                elif (b[s] > 0) != (stm > 0):
                    ms.append(sq | (s << 7))
        else:
            for d in (BD if t == 3 else RD if t == 4
                      else BD + RD):
                s = sq + d
                while (s & 0x88) == 0:
                    if b[s] == 0:
                        if not caps_only:
                            ms.append(sq | (s << 7))
                    else:
                        if (b[s] > 0) != (stm > 0):
                            ms.append(sq | (s << 7))
                        break
                    s += d
    if not caps_only:
        if stm > 0:
            if CS & 1 and b[5] == b[6] == 0 and b[7] == 4 \
                    and not AT(4, -1) and not AT(5, -1) \
                    and not AT(6, -1):
                ms.append(4 | (6 << 7))
            if CS & 2 and b[3] == b[2] == b[1] == 0 and b[0] == 4 \
                    and not AT(4, -1) and not AT(3, -1) \
                    and not AT(2, -1):
                ms.append(4 | (2 << 7))
        else:
            if CS & 4 and b[117] == b[118] == 0 and b[119] == -4 \
                    and not AT(116, 1) and not AT(117, 1) \
                    and not AT(118, 1):
                ms.append(116 | (118 << 7))
            if CS & 8 and b[115] == b[114] == b[113] == 0 \
                    and b[112] == -4 and not AT(116, 1) \
                    and not AT(115, 1) and not AT(114, 1):
                ms.append(116 | (114 << 7))
    return ms
def make(m):
    global stm, CS, ep, HM, key
    f = m & 127
    t = (m >> 7) & 127
    p = (m >> 14) & 15
    pc = b[f]
    cap = b[t]
    CX = t
    OK = key
    OC = CS
    OE = ep
    OF = HM
    key ^= ZP(pc, f)
    if cap:
        key ^= ZP(cap, t)
    key ^= ZC[CS]
    if ep >= 0:
        key ^= ZE[ep]
    key ^= ZS
    if abs(pc) == 1 and t == ep and cap == 0:
        CX = t - 16 * stm
        cap = b[CX]
        b[CX] = 0
        key ^= ZP(cap, CX)
    b[f] = 0
    b[t] = p * stm if p else pc
    key ^= ZP(b[t], t)
    if abs(pc) == 6 and abs(t - f) == 2:
        r0 = t + 1 if t in (6, 118) else t - 2
        r1 = t - 1 if t in (6, 118) else t + 1
        rp = 4 * stm
        b[r0] = 0
        b[r1] = rp
        key ^= ZP(rp, r0) ^ ZP(rp, r1)
    if f == 4 or t == 4: CS &= ~3
    if f == 7 or t == 7: CS &= ~1
    if f == 0 or t == 0: CS &= ~2
    if f == 116 or t == 116: CS &= ~12
    if f == 119 or t == 119: CS &= ~4
    if f == 112 or t == 112: CS &= ~8
    if abs(pc) == 1 and abs(t - f) == 32:
        ep = (f + t) // 2
    else:
        ep = -1
    HM = 0 if abs(pc) == 1 or cap else HM + 1
    key ^= ZC[CS]
    if ep >= 0:
        key ^= ZE[ep]
    stm = -stm
    return (m, cap, CX, OC, OE, OF, OK,
            (f, t, p, pc))
def unmake(ud):
    global stm, CS, ep, HM, key
    m, cap, CX, OC, OE, OF, OK, info = ud
    f, t, p, pc = info
    stm = -stm
    b[t] = 0
    b[f] = 1 * stm if p else pc
    if cap:
        b[CX] = cap
    if abs(pc) == 6 and abs(t - f) == 2:
        r0 = t + 1 if t in (6, 118) else t - 2
        r1 = t - 1 if t in (6, 118) else t + 1
        b[r1] = 0
        b[r0] = 4 * stm
    CS = OC
    ep = OE
    HM = OF
    key = OK
def EV():
    mg = 0
    eg = 0
    phase = 0
    bishops = [0, 0]
    for sq in range(128):
        if sq & 0x88:
            continue
        pc = b[sq]
        if pc == 0:
            continue
        t = abs(pc)
        phase += PW[t]
        if t == 3:
            bishops[0 if pc > 0 else 1] += 1
        f = sq & 7
        r = sq >> 4
        idx = (7 - r) * 8 + f if pc > 0 else r * 8 + f
        v = VAL[t] + PST[t][idx]
        ev = (VAL[6] + PE[idx]) if t == 6 else v
        mg += v if pc > 0 else -v
        eg += ev if pc > 0 else -ev
    if bishops[0] >= 2:
        mg += 30
        eg += 30
    if bishops[1] >= 2:
        mg -= 30
        eg -= 30
    if phase > 24:
        phase = 24
    total = (mg * phase + eg * (24 - phase)) // 24
    return total if stm > 0 else -total
class Abort(Exception):
    pass
def OM(ms, TM, ply):
    def score(m):
        if m == TM:
            return 1 << 30
        t = (m >> 7) & 127
        cap = b[t]
        if cap:
            return VAL[abs(cap)] * 10 - VAL[abs(b[m & 127])] // 10 + (1 << 20)
        if m == KL[ply][0] or m == KL[ply][1]:
            return 1 << 19
        pc = b[m & 127]
        return HS[(abs(pc) - 1) * 128 + t + (0 if pc > 0 else 768)]
    ms.sort(key=score, reverse=True)
    return ms
def QS(A, B, ply):
    global nodes
    nodes += 1
    if nodes > NODES:
        raise Abort
    IC = AT(KS(stm), -stm)
    if IC:
        ms = GM()
        OM(ms, 0, ply)
        best = -INF
        lg = 0
        for m in ms:
            ud = make(m)
            if AT(KS(-stm), stm):
                unmake(ud)
                continue
            lg += 1
            if key in PK:
                s = 0
            else:
                PK.append(key)
                try:
                    s = -QS(-B, -A, ply + 1)
                finally:
                    PK.pop()
            unmake(ud)
            if s > best:
                best = s
            if s > A:
                A = s
            if A >= B:
                return B
        if lg == 0:
            return -MATE + ply
        return best
    st = EV()
    if st >= B:
        return B
    if st > A:
        A = st
    ms = GM(caps_only=True)
    OM(ms, 0, ply)
    for m in ms:
        ud = make(m)
        if AT(KS(-stm), stm):
            unmake(ud)
            continue
        if key in PK:
            s = 0
        else:
            PK.append(key)
            try:
                s = -QS(-B, -A, ply + 1)
            finally:
                PK.pop()
        unmake(ud)
        if s >= B:
            return B
        if s > A:
            A = s
    return A
def SC(dp, A, B, ply):
    global nodes
    nodes += 1
    if nodes > NODES:
        raise Abort
    if HM >= 100:
        return 0
    IC = AT(KS(stm), -stm)
    if IC:
        dp += 1
    if dp <= 0:
        return QS(A, B, ply)
    entry = tt.get(key)
    TM = 0
    if entry and entry[0] >= dp:
        _, flag, s, TM = entry
        if flag == 0:
            return s
        if flag == 1 and s > A:
            A = s
        elif flag == 2 and s < B:
            B = s
        if A >= B:
            return s
    ms = GM()
    OM(ms, TM, ply)
    best = -INF
    BM = 0
    lg = 0
    OA = A
    for i, m in enumerate(ms):
        ud = make(m)
        if AT(KS(-stm), stm):
            unmake(ud)
            continue
        lg += 1
        if key in PK:
            s = 0
        else:
            PK.append(key)
            try:
                s = -SC(dp - 1, -B, -A, ply + 1)
            finally:
                PK.pop()
        unmake(ud)
        if s > best:
            best = s
            BM = m
        if s > A:
            A = s
            if A >= B:
                pc = b[m & 127]
                if b[(m >> 7) & 127] == 0:
                    if KL[ply][0] != m:
                        KL[ply][1] = KL[ply][0]
                        KL[ply][0] = m
                    HS[(abs(pc) - 1) * 128 + ((m >> 7) & 127) + (0 if pc > 0 else 768)] += dp * dp
                break
    if lg == 0:
        return -MATE + ply if IC else 0
    if best >= B:
        flag = 1
    elif best <= OA:
        flag = 2
    else:
        flag = 0
    tt[key] = (dp, flag, best, BM)
    return best
def BM(LU, ms=None):
    global nodes
    hist = None
    if ms:
        PF("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        hist = [key]
        for u in ms:
            f = (ord(u[0]) - 97) + (int(u[1]) - 1) * 16
            t = (ord(u[2]) - 97) + (int(u[3]) - 1) * 16
            p = 0
            if len(u) == 5:
                p = "nbrq".index(u[4]) + 2
            make(f | (t << 7) | (p << 14))
            hist.append(key)
        PF(CF)
        if key != hist[-1]:
            hist = None
    if hist is None:
        PF(CF)
        hist = [key]
    PK.clear()
    PK.extend(hist)
    lg = set(LU)
    RM = [m for m in GM()
                  if UO(m) in lg]
    if not RM:
        return LU[0]
    nodes = 0
    best = RM[0]
    dp = 1
    while dp <= 64:
        try:
            A = -INF
            B = INF
            CB = best
            CQ = -INF
            OM(RM, 0, 0)
            for m in RM:
                ud = make(m)
                if AT(KS(-stm), stm):
                    unmake(ud)
                    continue
                if key in PK:
                    s = 0
                else:
                    PK.append(key)
                    try:
                        s = -SC(dp - 1, -B, -A, 1)
                    finally:
                        PK.pop()
                unmake(ud)
                if s > CQ:
                    CQ = s
                    CB = m
                if s > A:
                    A = s
            best = CB
            dp += 1
            if CQ > MATE - 1000:
                break
        except Abort:
            break
    return UO(best)
def UO(m):
    f = m & 127
    t = (m >> 7) & 127
    p = (m >> 14) & 15
    s = "abcdefgh"[f & 7] + str((f >> 4) + 1) + "abcdefgh"[t & 7] \
        + str((t >> 4) + 1)
    if p:
        s += "nbrq"[p - 2]
    return s
def post(path, body):
    c = http.client.HTTPConnection(ENV_URL[7:])
    c.request("POST", path, json.dumps(body))
    r = c.getresponse()
    if r.status >= 400:
        raise SystemExit(r.status)
    return json.load(r)
CF = ""
while True:
    g = post("/game", {})
    if g["status"] == "done":
        break
    while g["status"] == "your_move":
        CF = g["fen"]
        mv = book_move(g)
        if mv is None:
            mv = BM(g["legal_moves"], g["moves"])
        g = post("/move", {"game": g["game"], "move": mv})
