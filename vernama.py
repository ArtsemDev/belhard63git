def load_key_msg_pair() -> tuple[str, str]:
    with (
        open("key.txt", "r", encoding="utf-8") as key_file,
        open("msg.txt", "r", encoding="utf-8") as msg_file,
    ):
        key = key_file.read().strip()
        msg = msg_file.read().strip()
        return key, msg


def encrypt_vernama(key: str, msg: str) -> str:
    # VAR 1
    key_bin = ""
    msg_bin = ""
    encrypt_msg = ""
    for i in range(len(key)):
        key_bin += bin(ord(key[i]))[2:].zfill(8)
        msg_bin += bin(ord(msg[i]))[2:].zfill(8)
    for i in range(len(key_bin)):
        if key_bin[i] == msg_bin[i]:
            encrypt_msg += "0"
        else:
            encrypt_msg += "1"
    return encrypt_msg
    # VAR 2
    # encrypt_msg = ''
    # for i in range(len(key)):
    #     encrypt_msg += bin(ord(key[i]) ^ ord(msg[i]))[2:].zfill(8)
    # return encrypt_msg


if __name__ == "__main__":
    print(encrypt_vernama(*load_key_msg_pair()))
