import os
os.system('cls')
import fractions
import logging
import argparse

FORMAT = '{levelname:} - время записи: {asctime}, функция: {funcName:>12} , {msg}'
logging.basicConfig(format=FORMAT, filename='logger_frac.log', 
                    encoding='UTF-8', level=logging.INFO, 
                    filemode='w', style='{'
                )
logger = logging.getLogger(__name__)


class Fractions:
    def __init__(self, chisl: int, znam: int) -> None:
        self.chisl = chisl
        self.znam = znam

    def frac_create(self):
        logger.info(f"создана дробь {self.chisl}/{self.znam}")        
        return fractions.Fraction(self.chisl, self.znam)
    
    def frac_mult(self, other: 'Fractions'):
        """ Функция умножения дробей """      
        a = (f"{self.chisl}/{self.znam}")
        b = (f"{other.chisl}/{other.znam}")
        с = (f"{self.chisl * other.chisl}/{self.znam * other.znam}")
        logger.info(f"результат произведения {a} и {b}: {с}")
        return f'{self.chisl * other.chisl}/{self.znam * other.znam}'
    
    def __add__(self, other: 'Fractions'):
        """ Функция сложения дробей """
        a = (f"{self.chisl}/{self.znam}")
        b = (f"{other.chisl}/{other.znam}")
        res_add = (fractions.Fraction(self.chisl, self.znam) 
                + fractions.Fraction(other.chisl, other.znam))
        logger.info(f"результат сложения {a} и {b}: {res_add}")
        return (res_add)
    
    def __str__(self) -> str:
        return f'{self.chisl}/{self.znam}'
    
def parser():
    pars = argparse.ArgumentParser(prog='Fractions()')
    pars.add_argument('-ch', default=1)
    pars.add_argument('-zn', default=1)        
    args = pars.parse_args()
    return Fractions(int(args.ch), int(args.zn)) 
    
if __name__ == "__main__":    
    fr1 = Fractions(1, 2)
    fr2 = Fractions(1, 3)   
    fr3 = Fractions(1, 4)

    fr1 + fr2
    fr3 + fr2
    fr1.frac_mult(fr2)
    fr1.frac_mult(fr3)

    # parser().frac_create()
    # parser().frac_mult(fr2)
    

