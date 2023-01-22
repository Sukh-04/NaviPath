"""Code within this file is to showcase the functional properties of the NaviPath Application.

=================================
This file is Copyright (c) 2022 Sukhjeet Singh Nar, Aabha Roy"""

import csv
from dataclasses import dataclass

import cohere

###############################################################################
# Class Defintions & Data Processing
###############################################################################
places_data_file = "TorontoData/Edited-Toronto-Places.csv"


@dataclass
class CityData:
    """A data class representing places to visit within
    the city of Toronto.

    Instance Attributes:
        - name: the name of places available to the public
        - preference: user preference of what they wish to explore
        - address: full address of the places
        - municipality: the municiplity the user-specified locations falls in
        - ward: the ward the user-specified locations falls in
        - description: short description of what to expect from the location
    """
    name: str
    preference: str
    address: str
    municipality: str
    ward: str
    description: str


def load_visit_data(filename: str) -> list[CityData]:
    """Return a list of Toronto attaction data based on the data in filename.

    The returned list must match the same order the rows appear in the given file.

    Preconditions:
    - filename refers to a csv file whose format matches the city dataset description
      on the assignment handout.

    >>> data = load_visit_data(places_data_file)
    >>> len(data)
    174
    """
    data_so_far = []

    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')

        # Skip the first header row.
        next(reader)

        for row in reader:
            # row is a list of strings
            # Your task is to extract the relevant data from row and add it to the accumulator.
            # Make sure to use type conversion to ensure instance attributes have the correct type
            row_data = CityData(
                name=row[0],
                preference=row[1],
                address=row[2],
                municipality=row[3],
                ward=row[4],
                description=row[5]
            )
            list.append(data_so_far, row_data)

    return data_so_far

###############################################################################
# Manipulations with Data
###############################################################################


def cohere_generate(preference: str) -> None:
    """Each call to this function allows individuals to generate information regarding """

    co = cohere.Client('o1y3ZA7jpDWgiqtwXMaW5RkSbBN6zoN0f9uSiAVl')  # This is your trial API key

    response = co.generate(
        model='80224565-40db-4f47-a062-f5097ac3d33f-ft',
        prompt='Given a user preference, this program will generate places to visit within Toronto.'
               '\n\nPreference: Attraction \nPlace: Casa Loma \n--  \nPreference: Attraction \nPlace: '
               'CN Tower\n-- \nPreference: Attraction \nPlace: Hockey Hall of Fame \n-- \nPreference: '
               'Attraction \nPlace: Ontario Science Centre \n-- \nPreference: Attraction \nPlace: Ripley\'s '
               'Aquarium of Canada\n-- \nPreference: Attraction \nPlace: Toronto Zoo \n-- \nPreference: Gallery '
               '\nPlace: Art Gallery of Ontario \n-- \nPreference: Gallery \nPlace: Canadian Sculpture Centre\n-- '
               '\nPreference: Museum \nPlace: Aga Khan Museum \n-- \nPreference: Museum \nPlace: Royal Ontario Museum '
               '\n-- \nPreference: Museum \nPlace: The Bata Shoe Museum \n-- \nPreference: Nature/ Park \nPlace: Allan '
               'Gardens\n-- \nPreference: Nature/ Park\nPlace: Bluffer\'s Park and Beach (Scarborough Bluffs)'
               '  \n-- \nPreference: Nature/ Park\nPlace: Gibraltar Point Beach \n-- \nPreference: Nature/Park\nPlace: '
               'Guild Park and Gardens \n-- \nPreference: Nature/ Park \nPlace: High Park \n-- \nPreference: Nature/ '
               'Park \nPlace: HTO Park \n-- \nPreference: Nature/ Park\nPlace: Humber Bay Park (Humber Bay Butterfly '
               'Habitat)'
               '\n-- \nPreference: Nature/ Park\nPlace: Kew Gardens Park \n-- \nPreference: Nature/ Park \nPlace: '
               'Riverdale Park (East and West) \n-- \nPreference: Nature/ Park \nPlace: Rosetta McClain Gardens \n-- \n'
               'Preference: Nature/ Park\nPlace: Toronto Botanical Gardens and Edwards Gardens  \n-- \nPreference: '
               'Nature/ Park\nPlace: Ward\'s Island Beach \n-- \nPreference: Performing Arts \nPlace: Berkeley Street '
               'Theatre\n-- \nPreference: Performing Arts\nPlace: Factory Theatre\n-- \nPreference: Performing '
               'Arts\nPlace: Four Seasons Centre for the Performing Arts \n-- \nPreference: Performing Arts \nPlace: '
               'Harbourfront Centre \n-- \nPreference: Performing Arts \nPlace: Hart House Theatre \n-- \n'
               + preference + ':',
        max_tokens=5,
        temperature=0.6,
        p=0.75
    )
    print('Prediction: {}'.format(response.generations[0].text))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
