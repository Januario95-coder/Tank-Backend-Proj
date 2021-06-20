
# PROBABILITY FACTOR DATA BOTTOM PLATES
# Action Taken to Limit Corrosion on Bottom Plates

IMPRE_CATHODIC_PROTECTION = [
    ('All readings around the periphery > 0.85 V - Score=0',
     'All readings around the periphery > 0.85 V'),
    ('0.6 V < All readings around the periphery < 0.85 V - Score=1',
     '0.6 V < All readings around the periphery < 0.85 V'),
    ('All readings around periphery < 0.6 V or CP doesn\'t exist - Score=2',
     'All readings around periphery < 0.6 V or CP doesn\'t exist')
]
SACRIFICIAL_CATHODIC_PROPECTION = [
    ('Sacrificial CP available and operating - Score=0',
     'Sacrificial CP available and operating'),
    # ('Sacrificial CP not applicable - Score=0', 'Sacrificial CP not applicable'),
    ('Sacrificial CP not available and nor operating - Score=2',
     'Sacrificial CP not available and nor operating')
]
BOTTOM_PLATES_INTERNAL_COATING_OR_LINING = [
    ('Internal coating applied and quality is sound - Score=0',
     'Internal coating applied and quality is sound'),
    ('Internal coating applied but quality is poor - Score=1',
     'Internal coating applied but quality is poor'),
    ('No coating is applied - Score=2', 'No coating is applied')
]
BOTTOM_PLATES_EXTERNAL_COATING = [
    ('External coating applied and quality is sound - Score=0',
     'External coating applied and quality is sound'),
    ('External coating applied but quality is poor - Score=1',
     'External coating applied but quality is poor'),
    ('No coating is applied - Score=2', 'No coating is applied')
]


# Features That Influences The Failure Mechanism of Bottom Plates

DEGREE_SIGN = u'\N{DEGREE SIGN}'


STORAGE_CONDITIONS = [
    (f'Temperature of product < 40{DEGREE_SIGN}C - Score=0',
     f'Temperature of product < 40{DEGREE_SIGN}C'),
    (f'Temperature of product between 40{DEGREE_SIGN}C and 85{DEGREE_SIGN}C - Score=1',
     f'Temperature of product between 40{DEGREE_SIGN}C and 85{DEGREE_SIGN}C'),
    (f'Temperature of product > 85{DEGREE_SIGN}C - Score=2',
     f'Temperature of product > 85{DEGREE_SIGN}C')
]
TYPE_OF_BOTTOM = [
    ('Cone up - Score=0', 'Cone up'),
    ('Flat - Score=2', 'Flat'),
    ('Cone down - Score=2', 'Cone down')
]
HEATING_COILS_IN_TANK = [
    ('No heating coil or no contact between heating coil and bottom plates - Score=0',
     'No heating coil or no contact between heating coil and bottom plates'),
    ('Presence of heating coil in direct contact with bottom plates - Score=1',
     'Presence of heating coil in direct contact with bottom plates')
]
PRODUCT_CORROSIVITY = [
    ('Slops, corrosive or aggresive chemical, raw water, brine (Unprotected) - Score=2', 'Slops, corrosive or aggresive chemical, raw water, brine (Unprotected)'),
    ('Slops, corrosive or aggresive chemical, raw water, brine (Internally protected) - Score=1', 'Slops, corrosive or aggresive chemical, raw water, brine (Internally protected)'),
    ('Fatty acids like Bio-fuels, Palm Oil (Unprotected) - Score=2', 'Fatty acids like Bio-fuels, Palm Oil (Unprotected)'),
    ('Fatty acids like Bio-fuels, Palm Oil (Internally protected) - Score=1', 'Fatty acids like Bio-fuels, Palm Oil (Internally protected)'),
    ('Crude Oil (unprotected) - Score=1', 'Crude Oil (unprotected)'),
    ('Crude Oil (Internally protected) - Score=0', 'Crude Oil (Internally protected)'),
    ('Gas Oil, Lube Oil, Diesel Oil, Caustic soda, Inert or nonaggressive chemicals, Ethanol, Methanol, air foam liquid, non-heated fuel oil. - Score=0', 'Gas Oil, Lube Oil, Diesel Oil, Caustic soda, Inert or nonaggressive chemicals, Ethanol, Methanol, air foam liquid, non-heated fuel oil.'),
    ('Jet A1 (fully internally protected) - Score=0', 'Jet A1 (fully internally protected)'),
    ('Light products, Kerosene, Gasoline, Cracked distillates, treated water (not internally protected) - Score=0', 'Light products, Kerosene, Gasoline, Cracked distillates, treated water (not internally protected)'),
    ('Heated products like Class D, E and F fuels in accordance with BS 2869 - Score=1', 'Heated products like Class D, E and F fuels in accordance with BS 2869'),
    ('Sulphur + heated products like Class G and H fuels in accordance with BS 2869 - Score=2', 'Sulphur + heated products like Class G and H fuels in accordance with BS 2869'),
    ('De-min Water - Score=1', 'De-min Water'),
    ('De-min Water (Fully protected) - Score=0', 'De-min Water (Fully protected)'),
    ('Products with unknown corrosion rates - Score=2', 'Products with unknown corrosion rates'),
]


# Effectiveness of Drainage To Prevent Water Ingress
# Under Bottom Plates

FOUNDATION_TYPE = [
    ('Traditional granular soil / sand type - Score=2', 'Traditional granular soil / sand type'),
    ('Sand pad with annular ring of coarse granular material - Score=1.33', 'Sand pad with annular ring of coarse granular material'),
    ('Sand pad with annular ring of coarse granular material and with sound sand/bitumen top layer - Score=0.67',
     'Sand pad with annular ring of coarse granular material and with sound sand/bitumen top layer'),
    ('Concrete raft under tank - Score=0',
     'Concrete raft under tank'),
    ('Piled concrete raft - Score=0',
     'Piled concrete raft')
]
HEIGHT_OF_FOUNDATION = [
    ('Height of the foundation is adequate to ensure a dry tank bottom - Score=0',
     'Height of the foundation is adequate to ensure a dry tank bottom'),
    ('Height of the foundation is not adequate to ensure a dry tank bottom - Score=2',
     'Height of the foundation is not adequate to ensure a dry tank bottom')
]
EFFECTIVENESS_OF_DRAINAGE = [
    ('Slope of tank pad shoulder allows for adequate drainage away from tank bottom - Score=0',
     'Slope of tank pad shoulder allows for adequate drainage away from tank bottom'),
    ('Water will remain under the tank bottom due to inadequate drainage or tank bottom is standing in water - Score=2',
     'Water will remain under the tank bottom due to inadequate drainage or tank bottom is standing in water')
]


# CONSEQUENCE FACTOR DATA BOTTOM PLATES

# Economic Aspects

TIME_TO_REPAIR = [
    ('No internal entry required, limited repair, no limitation on repair time - Score=1',
     'No internal entry required, limited repair, no limitation on repair time'),
    ('Internal entry required, limited repair (<3 months) - Score=2',
     'Internal entry required, limited repair (<3 months)'),
    ('Internal entry required, major repair (3-8 months)- Score=3',
     'Internal entry required, major repair (3-8 months)'),
    ('Internal entry required, major repair (>8 months)- Score=4',
     'Internal entry required, major repair (>8 months)')
]
COST_OF_REPAIR = [
    ('Negligible or less than 5% of capital cost - Score=1',
     'Negligible or less than 5% of capital cost'),
    ('5-10% of capital cost - Score=2', '5-10% of capital cost'),
    ('10-50% of capital cost - Score=3', '10-50% of capital cost'),
    ('>50% of capital cost (new tank) - Score=4', '>50% of capital cost (new tank)')
]
PROBABLE_MAGNITUDE_OF_PRODUCT_LOSS = [
    ('No release of product - Score=1', 'No release of product'),
    ('<5% of tank contents - Score=2', '<5% of tank contents'),
    ('>5% of tank contents - Score=3', '>5% of tank contents')
]


# Health and Safety Aspects

LIKELIHOOD_OF_INJURY_TO_PERSONNEL = [
    ('No injury or near miss - Score=1', 'No injury or near miss'),
    ('Minor injury - Score=2', 'Minor injury'),
    ('Lost time injury/Medical treatment - Score=3',
     'Lost time injury/Medical treatment'),
    ('Seriuos injury/fatality on site - Score=4', 'Seriuos injury/fatality on site')
]
PRODUCT_FLAMMABILITY_AS_PER_MCSP = [
    ('Class III(1) and unclassified product - Score=1',
     'Class III(1) and unclassified product'),
    ('Class II(1) product - Score=2', 'Class II(1) product'),
    ('Class II(2) and Class III(2) product - Score=3', 'Class II(2) and Class III(2) product'),
    ('Class I product - Score=4', 'Class I product'),
]
PRODUCT_TOXICITY = [
    ('Non-toxic substance- Score=1', 'Non-toxic substance'),
    ('Toxic substance if in contact with other substances - Score=2',
     'Toxic substance if in contact with other substances'),
    ('Toxic substance - Score=3', 'Toxic substance'),
    ('Extremely toxic substance - Score=4', 'Extremely toxic substance')
]
LOCATION_OF_TANK_FARM = [
    ('Tank farm within an abandonned area - Score=1',
     'Tank farm within an abandonned area'),
    ('Flat tank farm - Score=2', 'Flat tank farm'),
    ('Sloping tank farm - Score=3', 'Sloping tank farm'),
    ('In plant area within populous area - Score=4',
     'In plant area within populous area')
]
TANK_LOCATED_NEAR_A_PUBLIC_FENCE = [
    ('No - Score=0', 'No'),
    ('Yes - Score=1', 'Yes')
]
# CONTINUED_LOCATION_OF_TANK_FARM = [
# ('No public fence near tank farm', 'No public fence near tank farm'),
# ('Presence of public fence near tank farm', 'Presence of public fence near tank farm')
# ]


# Environmental Aspects
ENVIRONMETAL_HAZARD_TO_SOIL_AND_WATER_AS_THE_POTENTIAL_TO_CAUSE = [
    ('No or negligible environment effect - Score=1',
     'No or negligible environment effect'),
    ('Environmental nuisance affecting neighbourhood - Score=2',
     'Environmental nuisance affecting neighbourhood'),
    ('Environmental pollution, Extensive restoration required - Score=3',
     'Environmental pollution, Extensive restoration required'),
    ('Severe damage/nuisance/pollution over large area- Score=4',
     'Severe damage/nuisance/pollution over large area')
]
VAPOUR_EMISSION = [
    ('No or negligible harmful (toxic) release - Score=1',
     'No or negligible harmful (toxic) release'),
    ('Small harmful (toxic) release - Score=2', 'Small harmful (toxic) release'),
    ('Large (>1000m3) harmful (toxic) release - Score=3',
     'Large (>1000m3) harmful (toxic) release')
]


# INSPECTION DATA
ACCELERATION_FACTOR_FOR_PITTING = [
    ('CR ≥ 0.5mm (0.020 in.) /year - Score=1.15', 'CR ≥ 0.5mm (0.020 in.) /year'),
    ('0.3 mm (0.013 in.) ≤ CR < 0.5mm (0.020 in.) /year - Score=1.1',
     '0.3 mm (0.013 in.) ≤ CR < 0.5mm (0.020 in.) /year'),
    ('0.1 mm (0.004 in.) ≤ CR < 0.3mm (0.013 in.) /year - Score=1.05',
     '0.1 mm (0.004 in.) ≤ CR < 0.3mm (0.013 in.) /year'),
    ('CR < 0.1mm (0.004 in.)/year - Score=1.0', 'CR < 0.1mm (0.004 in.)/year')
]

ARE_PROCEDURES_IN_PLACE_TO_PREVENT_WATER_CONTACT = [
    ('Yes - Score=1', 'Yes'),
    ('No - Score=0', 'No')
]
IS_THE_CORROSION_RATE_DETERMINED_WITH_AT_LEAST_2_SOURCES = [
    ('Yes - Score=1', 'Yes'),
    ('No - Score=0', 'No')
]
IS_THE_DEGRADATION_SPEED_CALCULATED_BY_USING_AT_LEAST_3_MEASUREMENT_POINTS = [
    ('Yes - Score=1', 'Yes'),
    ('No - Score=0', 'No')
]
WHICH_METHOD_IS_USED = [
    ('LS fit - Score=0.6', 'LS fit'),
    ('Last 2 Points - Score=0.5', 'Last 2 Points'),
    ('Literature - Score=0', 'Literature'),
    ('Similar Service - Score=1', 'Similar Service'),
    ('2 Methods Used - Score=1', '2 Methods Used')
]



# Inspections
NDT_METHOD_USED_FOR_THICKNESS_MEASUREMENTS = [
    ('Floor scan + US - Score=1', 'Floor scan + US'),
    ('US on gridline system - Score=0.5', 'US on gridline system'),
    ('Visual + Spot ultrasonic (US) - Score=0)',
     'Visual + Spot ultrasonic (US)')
]
FREQUENCY_OF_INTERNAL_INSPECTIONS_PERFORMED_DURING_SERVICE_LIFE = [
    ('Multiple inspections carried out - Score=1',
     'Multiple inspections carried out'),
    ('One or two inspections carried out - Score=0.5',
     'One or two inspections carried out'),
    ('No or minimal inspection data available - Score=0',
     'No or minimal inspection data available')
]
NDT_METHOD_AND_QUALIFICATION_OF_NDT_OPERATORS_IN_PLACE_AND_ASSESSED = [
    ('Yes - Score=1', 'Yes'),
    ('No - Score=0', 'No')
]

IS_THE_CONSTRUCTION_SUCH_THAT_CORROSION_MAY_BE_REDUCED_BY_THE_CHOSEN_WELD_CONFIGURATION = [
    ('Annual plates butt welded with backing strip - Score=1.0', 'Annual plates butt welded with backing strip'),
    ('Annular plates butt welded from both sides - Score=0.75', 'Annular plates butt welded from both sides'),
    ('No annular section, but double pass lap welded sketch plates - Score=0.50', 'No annular section, but double pass lap welded sketch plates'),
    ('No annular section but single pass lap welds sketch plates - Score=0.25', 'No annular section but single pass lap welds sketch plates'),
]



# Maturity of the Assessment
IS_EVIDENCE_AVAILABLE_OF_COMPLETING_PDCA_CYCLE_ON_INSPECTION_ACTIVITIES = [
    ('Yes - Score=1', 'Yes'),
    ('No - Score=0', 'No')
]
DOES_THE_ORGANISATION_HAVE_THE_PROPER_QUALIFICATIONS_TO_DETERMINE_DEGRADATIONS_SPEEDS_AND_ASSESS_INSPECTION_RESULTS = [
    ('Yes - Score=1', 'Yes'),
    ('No - Score=0', 'No')
]
ARE_RESULTS_ALWAYS_DISCUSSED_IN_A_MULTIDISCIPLINARY_RBI_TEAM = [
    ('Yes - Score=1', 'Yes'),
    ('No - Score=0', 'No')
]
ARE_TRAINING_REQUIREMENTS_FOR_RBI_TEAM_MEMBERS_CONSISTENTLY_USED = [
    ('Yes - Score=1', 'Yes'),
    ('No - Score=0', 'No')
]


# Predictability of the Mechanism
DOES_THE_ITEM_EVALUATION_HAVE_SIGNIFICANT_PITTING = [
    ('Yes - Score=0', 'Yes'),
    ('No - Score=1', 'No')
]
CAN_THE_DEGRADATION_MECHANISM_BE_REGARDED_AS_LINEAR = [
    ('Yes - Score=1', 'Yes'),
    ('No - Score=0', 'No')
]
