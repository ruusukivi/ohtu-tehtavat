class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujoukko = [0] * self.kapasiteetti
        self.lukujen_maara = 0

    def sisaltyy_joukkoon(self, luku):
        if luku in self.lukujoukko:
                return True
        return False

    def lisaa_luku(self, luku):
        if not luku in self.lukujoukko:
            self.lukujoukko[self.lukujen_maara] = luku
            self.lukujen_maara = self.lukujen_maara + 1

        if self.lukujen_maara % len(self.lukujoukko) == 0:
            self.kasvata_joukon_kokoa()

    def poista_luku(self, luku):
        if luku in self.lukujoukko:
            self.lukujoukko.remove(luku)
            self.lukujen_maara = self.lukujen_maara - 1

    def kasvata_joukon_kokoa(self):            
        aiempi_joukko = self.lukujoukko
        self.lukujoukko = [0] * (self.lukujen_maara + self.kasvatuskoko)
        self.kopioi_taulukko(aiempi_joukko, self.lukujoukko)

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def joukon_lukujen_maara(self):
        return self.lukujen_maara

    def joukon_luvut(self):
        luvut = [0] * self.lukujen_maara
        for i in range(0, len(luvut)):
            luvut[i] = self.lukujoukko[i]
        return luvut

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.joukon_luvut()
        b_taulu = b.joukon_luvut()

        for i in range(0, len(a_taulu)):
            yhdiste.lisaa_luku(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste.lisaa_luku(b_taulu[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.joukon_luvut()
        b_taulu = b.joukon_luvut()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus.lisaa_luku(b_taulu[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.joukon_luvut()
        b_taulu = b.joukon_luvut()

        for i in range(0, len(a_taulu)):
            erotus.lisaa_luku(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus.poista_luku(b_taulu[i])

        return erotus

    def __str__(self):
        if self.lukujen_maara == 0:
            return "{}"
        elif self.lukujen_maara == 1:
            return "{" + str(self.lukujoukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.lukujen_maara - 1):
                tuotos = tuotos + str(self.lukujoukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujoukko[self.lukujen_maara - 1])
            tuotos = tuotos + "}"
            return tuotos
