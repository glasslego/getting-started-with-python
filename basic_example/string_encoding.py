def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = " ".join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = " ".join("{0}".format(int(c)) for c in byte_data)

    print("'" + text + "' 전체 문자 길이: {0}".format(len(text)))
    print(
        "'"
        + text
        + "' 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트".format(
            len(byte_data)
        )
    )
    print("'" + text + "' 16진수 값: {0}".format(hex_data_as_str))
    print("'" + text + "' 10진수 값: {0}".format(int_data_as_str))


def read_binary_data():
    # 2진수를 10진수로 처리
    print(f"10진수(01000001)={0b01000001}")
    # 2진수를 16진수로 처리
    print(f"16진수(01000001)={hex(0b01000001)}")
    # 2진수를 문자로 처리
    print(f"문자(01000001)={chr(0b01000001)}")


if __name__ == "__main__":
    print("\n------ ascii 인코딩 ------")
    print_text("Hello", "ascii")
    # ascii 인코딩은 한글을 지원하지 않으므로 주석 처리
    # print_text('안녕하세요', 'ascii')

    print("\n------ euc-kr 인코딩 ------")
    print_text("Hello", "euc-kr")
    print_text("안녕하세요", "euc-kr")

    print("------ utf-8 인코딩 ------")
    print_text("Hello", "utf-8")
    print_text("안녕하세요", "utf-8")

    print("\n------ utf-16 인코딩 ------")
    print_text("Hello", "utf-16")
    print_text("안녕하세요", "utf-16")

    print("\n------ binary data ------")
    read_binary_data()
