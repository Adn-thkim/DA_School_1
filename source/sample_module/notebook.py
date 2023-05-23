# 노트 기능 (노트는 노트북의 일부)

class Note():
    '''맨 처음은 초기화를 시켜야하기 때문에 write = none'''
    def __init__(self, write = None):
        self.write = write
    '''쓰는 기능 추가'''
    def write_function(self, write):
        self.write = write
    '''모두 지우는 기능 추가'''
    def remove_all(self):
        self.write = ""
    '''작성된 내용 출력'''
    def __str__(self):
        return self.write
    
# 노트북의 기능

class NoteBook():
    '''모든 기능을 저장하기 위해 다음과 같이 __init__에 모두 입력'''
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {} # 딕셔너리 형으로 선언 Note Page Number를 Key로 설정해서 쉽게 찾기 위함

    ''' 새로운 노트를 노트북에 추가하는 함수'''
    ''' 지금은 되게 기본 기능만 추가했지만 실제 기능구현시 많은 것을 고려해야함 '''
    ''' 7페이지면 8페이지에 추가되는 형태로 일단 구현'''
    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.note[self.page_number] = note
                self.page_number += 1

            else:
                self.notes = {page : note}
                self.page_number += 1
        else:
            print("페이지가 300페이지가 넘어서 추가할 수 없어요")

    ''' 특정 페이지 번호에 있는 노트를 제거하는 함수'''
    # 딕셔너리의 Key가 있는 지확인하고, 있다면 삭제 없으면 프린트문 사용해서 경고문장 출력
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("삭제된 노트입니다.")

    # 현재 노트 페이지 출력
    def get_number_of_page(self):
        return len(self.notes.keys())

########### 실습 종료 ###########
##############################