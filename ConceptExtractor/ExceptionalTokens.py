class ExceptionalTokens():
    """This class is used to hold all lists of words that are either abbreviations, acronyms etc and those that are exceptional words
    whihc should not be treated as concepts"""
    abbreviations=[]
    nonConceptBearingTerms=[]

    def __init__(self):
        self.abbreviations=['komp','ltg','ra','sonstige','ausdr','farbschattierg','tiern','vkdl','füg','tieren','ähnl'
                       'krankheitsn','vergleiche', 'farbbez','kh','fech','kch','volkstüml','heraus','z.B.','en']
        self.nonConceptBearingTerms=['bedeutungen','üblich','wendungen','ausdrücke','ganzes','ja','abfarb']

    def loadAbbreviations(self, fileName):
        """The method allows loading a csv abbreviation file to """
    #     add the code to read from a file and load the data as abbreviations array.
        pass

    def loadNonContentBearingTerms(self, fileName):
        """The method allows loading a csv abbreviation file to """
    #     add the code to read from a file and load the data as abbreviations array.
        pass

    def getAbbreviations(self):
        """Returns all the abbreviations that are loaded here. The source could be either hard coded abbreviations or abbreviations from a file"""
        return self.abbreviations

    def getNonConceptBearingTerms(self):
        """Returns all the nonconceptbearing words that are loaded here. The source could be either hard coded  or terms from a file"""
        return self.nonConceptBearingTerms