vow = {"a":"1", "e":"2", "i":"3", "o":"4", "u":"5"}

def encode(st):
    for w in vow:
        st = st.replace(w, vow[w])
    return st

def decode(st):
    for k,v in vow.items():
        st = st.replace(v, k)
    return st