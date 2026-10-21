"""
IA_OCNEPI_ZOUBIROU - Souveraineté IA22
Chemin Termux: /data/data/com.termux/files/home/IA22CONSOLEDEPLOY/
Signature IA : IAOCNEPIZOUBIROU
"""

SIGNATURE_IA = "IAOCNEPIZOUBIROU"
ID_MODULE = "IA_OCNEPI_ZOUBIROU"
HOME_TERMUX = "/data/data/com.termux/files/home"

def get_signature():
    return SIGNATURE_IA

def verify_node():
    print(f" Node vérifié: {ID_MODULE} | Signature: {SIGNATURE_IA}")
    print(f" Home: {HOME_TERMUX}")
    return True

if __name__ == "__main__":
    verify_node()
