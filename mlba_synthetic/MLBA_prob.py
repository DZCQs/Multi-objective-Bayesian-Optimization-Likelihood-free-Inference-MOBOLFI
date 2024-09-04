from scipy.stats import norm


def cdf_per(rt, drift, b, A, s):
    """
    :param rt: float type. Response time.
    :param drift: float type. The drift rate mean of corresponding alternative.
    :param b: float type. The decision threshold.
    :param A: float type. The upper boundary of starting point.
    :param s: float type. The sd of noise.
    :return: float type. cdf of the corresponding alternative touch the threshold at rt.
    """
    cdf = 1 + (b - A - drift * rt) / A * norm.cdf((b - A - drift * rt) / (s * rt)) - (b - drift * rt) / A * norm.cdf(
        (b - drift * rt) / (s * rt)) + s * rt / A * norm.pdf((b - A - drift * rt) / (s * rt)) - s * rt / A * norm.pdf(
        (b - drift * rt) / (s * rt))
    cdf = cdf / norm.cdf(drift / s)
    if A < 1e-10:
        cdf = norm.cdf(b / rt, loc=drift, scale=s)
    return cdf


def pdf_per(rt, drift, b, A, s):
    """
     :param rt: float type. Response time.
     :param drift: float type. The drift rate mean of corresponding alternative.
     :param b: float type. The decision threshold.
     :param A: float type. The upper boundary of starting point.
     :param s: float type. The sd of noise.
     :return: float type. pdf of the corresponding alternative touch the threshold at rt.
     """
    pdf = (-drift * norm.cdf((b - A - drift * rt) / (s * rt)) + drift * norm.cdf((b - drift * rt) / (s * rt)) + s * norm.pdf(
        (b - A - drift * rt) / (s * rt)) - s * norm.pdf((b - drift * rt) / (s * rt))) / A

    pdf = pdf / norm.cdf(drift / s)
    if A < 1e-10:
        pdf = norm.pdf(b / rt, loc = drift, scale = s) * b / rt / rt
    return pdf


def pdf_mlba(rc, rt, drift, b, A, s):
    """
    :param rc: a list, length is nAlt.
            the element values 1 when corresponding alternative is selected, otherwise 0.
    :param rt: float type. Response time.
    :param drift: a list, length is nAlt.
            Each element is the drift rate mean for corresponding alternative.
    :param b: float type. Decision threshold.
    :param A: float type. The upper boundary of starting point.
    :param s: float type. The sd of noise.
    :return: float type. The pdf of choosing certain alternative at rt.
    """
    pdf_MLBA = 1
    nAlt = len(rc)
    for i in range(nAlt):
        if rc[i]!=1:
            pdf_MLBA *= 1-cdf_per(rt=rt, drift=drift[i], b=b, A=A, s=s)
        else:
            pdf_MLBA *= pdf_per(rt=rt, drift=drift[i], b=b, A=A, s=s)

    return pdf_MLBA