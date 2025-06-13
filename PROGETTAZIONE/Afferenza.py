from __future__ import annotations
from datetime import date
from typing import Self

class Impiegato:

    _nome:str
    _cognome:str
    _datadinascita:date

    def __init__(self, nome:str, cognome:str, datadinascita:date, stipendio:float):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._setdata(datadinascita)
        self._stipendio = stipendio
        self._progetti:set[Partecipa] = ()


    def set_nome(self, nome:str):

        self.nome = nome

    def set_cognome(self, cognome:str):

        self.cognome = cognome


    def _setdata(self, datadinascita:date):

        self.datadinascita = datadinascita

    def addlink(self, set:frozenset):

        self._progetti.add(set)
    
    def get_progetti(self) ->frozenset[Partecipa]:

        return frozenset(self._progetti)
    
    def add_link_partecipa(self, l:Partecipa._link) ->None:

        self._progetti.add(l)

    def _remove_link(self,):

        pass




    '''def _partecipazione_progetto(self, progetto:Progetto, datadipartecipazione:date):

        if (progetto, date) not in self._progetti_in_cuipartecipa:

            self._progetti_in_cuipartecipa.append((progetto,datadipartecipazione))

        else:

            print("Error, project already in memory")'''





class Progetto:
    _nome: str
    _budget: float
    _impiegati_partecipanti: set[Partecipa] #Non noto alla nascita

    def __init__(self, nome:str, budget:float):

        self.nome = nome 

        self._budget = budget

        #self._impiegati_partecipanti = []

        self._impiegati_partecipanti:set[Partecipa] = ()

    def impiegati(self) ->frozenset[Partecipa]:

        return frozenset(self._impiegati_partecipanti)
    
    def _add_link_partecipa(self, l:Partecipa._link)->None:

        self._impiegati_partecipanti.add(l)


    def _remove_link_partecipa(self, l:Partecipa._link):

        if l._progetto != self:

            raise ValueError("Il link non coinvolge me")
        
        else:

            self._impiegati_partecipanti.remove(l)


    #def addlink2(self, set:set):

        #self._impiegati_partecipanti.add(set)

        #return self._impiegati_partecipanti


    '''def _aggiungi_impiegato(self, impiegato:Impiegato, datapartecipazione:date):

        if (impiegato,datapartecipazione) not in self._impiegati_partecipanti:

            self._impiegati_partecipanti.append((impiegato,datapartecipazione))

            impiegato._partecipazione_progetto(self,datapartecipazione)

        else:

            print ("ERROR")'''


class Partecipa:

    @classmethod
    def add(cls, progetto:Progetto, impiegato:Impiegato, data_partecipazione:date) ->_link:

        l = cls._link(progetto,impiegato,data_partecipazione)

        progetto._add_link_partecipa(l)
        impiegato.add_link_partecipa(l)

        return(l)
    
    @classmethod
    def remove(cls,l:_link)->None:

        pass


    class _link:

        _progetto:Progetto #ovviamente immutabile e noto alla nascita
        _impiegato:Impiegato#ovviamente immutabile e noto alla nascita
        _data_partecipazione:date #immutabile, noto alla nascita

        def __init__(self,progetto:Progetto, impiegato:Impiegato, data_partecipazione:date):

            self._progetto = progetto
            self._impiegato = impiegato
            self._data_partecipazione = data_partecipazione 

            
        
        '''def link_progetto(cls, impiegato:Impiegato, progetto:Progetto, data_partecipazione:date):


            #impiegato._partecipazione_progetto(progetto, data_partecipazione)
            #progetto._aggiungi_impiegato(impiegato, data_partecipazione)

            link:set = (impiegato,progetto,data_partecipazione)

            link = frozenset(link)
            impiegato.addlink(link)
            progetto.addlink(link)



            return frozenset(link)'''
        


