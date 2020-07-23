import re
import PeriodicTable

class Element:
    def __init__(self, symbol, subscript=1):
        if symbol not in PeriodicTable.table:
            raise Exception("Not a valid element name.")
        self.symbol = symbol
        self.subscript = subscript

    def __str__(self):
        if self.subscript > 1:
            return self.symbol + "_"+ str(self.subscript)
        else:
            return self.symbol

class Compound:

    def __init__(self, pieces, coefficient=1):
        self.pieces = pieces
        self.coefficient = coefficient

    def __str__(self):
        return_string = ""
        for piece in self.pieces:
            if type(piece) == Compound and piece.coefficient > 1:
                    return_string += "(" + str(piece) + ")_" + str(piece.coefficient)
            else:
                return_string += str(piece)
        return return_string

    def get_element_count(self):
        elements = {}
        for piece in self.pieces:
            if type(piece) == Element:
                if(piece.symbol in elements):
                    elements[piece.symbol] += piece.subscript * self.coefficient
                else:
                    elements[piece.symbol] = piece.subscript * self.coefficient
            elif type(piece) == Compound:
                polyatomic_ion_element_dict = piece.get_element_count()
                for key in polyatomic_ion_element_dict:
                    if key in elements:
                        elements[key] += polyatomic_ion_element_dict[key]*self.coefficient
                    else: 
                        elements[key] = polyatomic_ion_element_dict[key] * self.coefficient
            else:
                raise Exception("Incompatible type")
        return elements

class Species:

    def __init__(self, compound, coefficient):
        self.compound = compound
        self.coefficient = coefficient


class Equation:

    def __init(self, reactants, products):
        self.reactants_species = reactants
        self.products_species = products

def parse_compound(input):
    if len(input) < 1:
        raise Exception("Invalid input")
    
    match = re.match(r"([1-9]?)([(]?[A-Z]+[a-z]?[)]?)([1-9]?)", input, re.I)
    if match:
        items = match.groups()
        print(input, ": ",items)

    

def parse_equation(input):
    #clean spaces
    input = input.replace(" ","")

    # split into 2 sides of the equation
    split_str = input.split("=")
    if len(split_str) != 2:
        return "Invalid input: string must contain 1 = to split the equation." 
    
    # Split into reactants and products.
    reactants = split_str[0].split("+")
    products = split_str[1].split("+")

    # Process reactants into list of compounds.
    reactant_compounds_list = []
    for reactant in reactants:
        compound = parse_compound(reactant)
        reactant_compounds_list.append(compound)

    # Process products into list of products.
    product_compounds_list = []
    for product in products:
        compound = parse_compound(product)
        product_compounds_list.append(compund)

    return (Equation(reactant_compounds_list, product_compounds_list))



calcium = Element("Ca")
nitrogen = Element("N")
oxygen = Element("O",3)



nitrate = Compound([nitrogen, oxygen],2)
calcium_nitrate = Compound([calcium, nitrate])


parse_compound("N")
parse_compound("Fe")
parse_compound("ClO3")
parse_compound("Na(ClO3)2")

