from os import system
system('cls')
import logging

FORMAT = '{levelname:<8} - время записи: {asctime}, строка срабатывания: {lineno:02d}, {msg}'
logging.basicConfig(format=FORMAT, filename='logger_student.log', 
                    encoding='UTF-8', level=logging.INFO, 
                    filemode='w', style='{'
                )
logger = logging.getLogger(__name__)

class Requirements:

    def __set_name__(self, owner, name):
            self.param_name =  '_' + name      

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
        
    def validate(self, value: str):
                       
        START_CAP_LETTER = 1040        
        FINISH_LOWERCASE = 1103
        if value == value.capitalize():
            for i in range(len(value)):
                cur_letter = ord(value[i])
                if (cur_letter < START_CAP_LETTER 
                    or cur_letter > FINISH_LOWERCASE):
                    logger.critical(f"ошибка ввода 'ValueError' - {value} ")            
                    raise ValueError(f'Ошибка ввода данных.')
        else:
            logger.critical(f"Ошибка ввода 'ValueError' - {value} ")            
            raise ValueError (f'ошибка ввода данных.')
            
class Student:
    _name = Requirements()
    _surname = Requirements()

    def __init__(self, _name: str, _surname: str):
        self._name = _name
        self._surname = _surname
        logger.info(f"в базу внесен студент - {_name} {_surname}")

if __name__ == "__main__":
    st1 = Student('Макс', 'Петров')
    st2 = Student('Вася', 'Пупкин')
    st4 = Student('Джон', 'Траволта')
    # st3 = Student('ваня', 'Сидоров')
    # st5 = Student('Мак1', 'Петров')


