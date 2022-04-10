from curses.ascii import isblank
from enum import Enum
from tkinter import ttk, constants, StringVar

edelliset = []

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovellus, self._lue_syote),
            Komento.EROTUS: Erotus(sovellus, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovellus, self._lue_syote),
            Komento.KUMOA: Kumoa(sovellus, self._lue_syote)
        }

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(
            columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        syote = self._syote_kentta.get()
        if syote == "":
            syote = 0
        return syote

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        if komento_olio:
           komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)


class Summa:
    def __init__(self, sovellus, syote):
        self.syote= syote
        self.sovellus = sovellus

    def suorita(self):
        edelliset.append(self.sovellus.tulos)
        return self.sovellus.plus(int(self.syote()))

class Erotus:
    def __init__(self, sovellus, syote):
        self.syote = syote
        self.sovellus = sovellus

    def suorita(self):
        edelliset.append(self.sovellus.tulos)
        return self.sovellus.miinus(int(self.syote()))

class Nollaus:
    def __init__(self, sovellus, syote):
        self.syote = syote
        self.sovellus = sovellus
    def suorita(self):
        edelliset.append(self.sovellus.tulos)
        return self.sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, syote):
        self.syote = syote
        self.sovellus = sovellus

    def suorita(self):
        if len(edelliset) > 0:
            self.sovellus.aseta_arvo(edelliset.pop())
        else:
            self.sovellus.aseta_arvo(0)
