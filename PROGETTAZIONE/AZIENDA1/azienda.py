from typing import Self, Any
from datetime import datetime,date
from future import Impiegato #Importazione della classe futura per problemi di utilizzo circolare


class RealGEZ(float):

    def __new__ (cls, v:int|float|str) -> Self:

        if v < 0:

            raise ValueError(f"Value v =={v} must be >= 0")
        
        return float.__new__(cls,v)
    


class RealGZ(RealGEZ):


    def __new__ (cls, v:int|float|str) -> Self:

        if v == 0:

            raise ValueError(f"Value must be greater than 0")
        
        return RealGEZ.__new__(cls,v)



class Dipartimento:

    def __init__(self):
        pass



class _Afferenza: #Abbiamo reso la classe "Protetta"

    _impiegato:Impiegato #<<Imm>>
    _dipartimento:Dipartimento #<<Imm>>
    _data_afferenza: datetime.date 


    def impiegato(self) ->Impiegato:
        return self._impiegato
    
    def dipartimento(self) ->Dipartimento:
        return self._dipartimento
    
    def data_afferenza(self) ->datetime.date:
        return self._data_afferenza
    
    def set_data_afferenza(self, v:datetime.date) ->None:

        self._data_afferenza = v


    def __init__(self, impiegato:Impiegato, dipartimento:Dipartimento, data_afferenza:datetime.date):

        self._impiegato = impiegato
        self._dipartimento = dipartimento
        self.set_data_afferenza (data_afferenza)

    def __hash__(self) ->int:
        return hash(self.impiegato(), self.dipartimento())

    def __eq__(self, other:Any):
        if type(self) != type(other):#not isinstance(other, _Afferenza):
            return False
        
        else:

            return self.impiegato() == other.impiegato() and self.dipartimento() == other.dipartimento()
        
        

class Impiegato:

    _nome:str
    _cognome:str
    _stipendio_annuale_eur:RealGZ
    _data_afferenza: datetime.date
    _nascita : datetime.date #<<IMMUTABILE>>ù
    _dipartimento:Dipartimento|None
    _afferenza:_Afferenza


    def nome(self) ->str:
        return self._nome
    
    def cognome(self) ->str:
        return self._cognome
    
    def stipendio_annuale_eur(self) ->RealGZ:
        return self._stipendio_annuale_eur
    
    #def data_afferenza(self) ->datetime.date:
        return self._data_afferenza
    
    def nascita(self) ->datetime.date:
        return self._nascita
    
    #def dipartimento(self) ->Dipartimento|None:
        #return self._dipartimento
    
    def set_nome(self, v:str) ->None:
        self._nome:str = str(v)

    def set_cognome(self, v:str) ->None:
        self._cognome:str = str(v)

    def set_stipendio_annuale_eur(self, v:RealGZ) ->None:
        self._stipendio_annuale_eur:RealGZ = RealGZ(v)

    def set_afferenza(self, dipartimento:Dipartimento, data_afferenza:datetime.date) ->None:
        self._afferenza = _Afferenza(self, dipartimento, data_afferenza)

    #def set_data_afferenzade(self, v:datetime.date) ->None:
        #self._data_afferenza = v

    #def set_nascita(self,v:...) <<-- NO, perchè immutabile e noto alla nascita

    #def set_dipartimento(self, v:Dipartimento) ->None:
        #self._dipartimento = v

    #def unset_dipartimento(self) ->None:
        #self._dipartimento = None



    #INCOMPLETO!! Manca l'inserimento del lint "afferenza"
    def __init__(self,*, nome:str, cognome:str, stipendio_annuale_eur:RealGZ, nascita:datetime.date, afferenza:_Afferenza , dipartimento:Dipartimento,data_afferenza:datetime.date ) ->Self: #dipartimento:Dipartimento, data_afferenza:datetime.date

        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_stipendio_annuale_eur(stipendio_annuale_eur)
        #self.set_data_afferenzade(data_afferenza)
        self.nascita = nascita
        self.set_afferenza(self, dipartimento, data_afferenza )
        #self.set_dipartimento(dipartimento)




'''Da impedire la creazione diretta di un link l= (i1, d1) o la creazione di link duplicati ''' #FATTO VV






        


    
    
    

