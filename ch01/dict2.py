def menu():
    for key, val in goods.items():
        print(f"{key}: {val:,}원")
    print()

def search():
    while True:
        인풋상품검색 = input("구매 상품을 입력하세요> ")
        # 여기 아래로는 GPT 돌림
        matching_items = [item for item in goods if 인풋상품검색 in item]
        if matching_items:
            if len(matching_items) > 1:
                print("다음과 같은 상품들이 검색되었습니다.\n")
                for item in matching_items:
                    print(f"{item} |", end=" ")
                print()
                print("\n더 구체적으로 입력해주세요.")
                continue

            상품명 = matching_items[0]
            # 여기 아래로는 직접함
            수량 = int(input("구매 수량을 입력하세요> "))
            상품가격 = 수량 * goods[상품명]
            배송비 = 2500
            if 상품가격 < 20000:
                합계 = 상품가격 + 배송비
                print(f"\n{상품명}의 가격은 {상품가격:,}원 이므로\n"
                      f"배송비 {배송비:,}원이 추가되어\n"
                      f"{합계:,}원 결제 됩니다.\n")
                break
            else:
                print(f"\n{상품명} {수량}개 {상품가격:,}원 입니다.")
                break
        else:
            print(f"\n입고된 상품만 판매됩니다.\n다시 입력해주세요.\n")
            continue


goods = {"수박": 19500, "귤": 2500, "돼지고기": 20000, "참외": 6000, "애플수박":8000}

menu()
search()
