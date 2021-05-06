
IMPRESSED_COATING_APPLIED_TO_SHEEL_PLATES = [
    ('Internal coating applied and quality is sound - score=0', 'Internal coating applied and quality is sound'),
    ('Internal coating applied and quality is poor - score=1', 'Internal coating applied and quality is poor'),
    ('Internal coating not existing - score=2', 'Internal coating not existing')
]
EXTERNAL_COATING_APPLIED_TO_SHELL_PLATES = [
    ('External coating applied and quality is sound - score=0', 'External coating applied and quality is sound'),
    ('External coating applied and quality is poor - score=1', 'External coating applied and quality is poor'),
    ('External coating not existing - score=2', 'External coating not existing')
]




DEGREE_SIGN = u'\N{DEGREE SIGN}'

STORAGE_CONDITIONS = [
    (f'Temperature of product < 40{DEGREE_SIGN}C - score=0', f'Temperature of product < 40{DEGREE_SIGN}C'),
    (f'40{DEGREE_SIGN}C Temperature of product < 85{DEGREE_SIGN}C - score=1', f'40{DEGREE_SIGN}C Temperature of product < 85{DEGREE_SIGN}C'),
    (f'Temperature of product > 85{DEGREE_SIGN}C - score=2', f'Temperature of product > 85{DEGREE_SIGN}C')
]
HEATING_COILS_IN_TANK = [
    ('No heating coil or no contact between heating coil and shell plates - score=0', 'No heating coil or no contact between heating coil and shell plates'),
    ('Presence of heating coil in direct contact with shell plates - score=1', 'Presence of heating coil in direct contact with shell plates')
]
PRODUCT_CORROSIVITY = [
    ('Group 1/Risk H - score=2', 'Group 1/Risk H'),
    ('Group 3/Risk M - score=1', 'Group 3/Risk M'),
    ('Group 4/Risk L - score=0', 'Group 4/Risk L'),
    ('Group 5/Risk L - score=0', 'Group 5/Risk L'),
    ('Group 6/Risk M - score=1', 'Group 6/Risk M')
]
VAPOUR_CORROSIVITY = [
    ('Group 1/Risk H - score=2', 'Group 1/Risk H'),
    ('Group 3/Risk M - score=1', 'Group 3/Risk M'),
    ('Group 4/Risk L - score=0', 'Group 4/Risk L'),
    ('Group 5/Risk L - score=0', 'Group 5/Risk L'),
    ('Group 6/Risk M - score=1', 'Group 6/Risk M')
]
TANK_SHELL_HAS_BEEN_INSULATED = [
    ('CUI is likely to occur - score=2', 'CUI is likely to occur'),
    ('Tank shell is properly insulated and CUI is unlikely to occur - score=0', 'Tank shell is properly insulated and CUI is unlikely to occur'),
    ('Tank shell is not insulated, - score=0', 'Tank shell is not insulated,')
]



CORROSION_UNDER_INSULATION_CUI = [
    ('Tank shell is not insulated - score=2', 'Tank shell is not insulated'),
    ('Tank shell is properly insulated and CUI is unlikely to occur - score=0', 'Tank shell is properly insulated and CUI is unlikely to occur'),
    ('CUI is likely to occur - score=0', 'CUI is likely to occur')
]





TIME_TO_REPAIR = [
    ('No internal entry required, limited repair - score=1, no limitation on repair time', 'No internal entry required, limited repair, no limitation on repair time'),
    ('Internal entry required, limited repair (<3 months) - score=2', 'Internal entry required, limited repair (<3 months)'),
    ('Internal entry required, major repair (3-8 months - score=3)', 'Internal entry required, major repair (3-8 months)'),
    ('Internal entry required, major repair (>8 months) - score=4', 'Internal entry required, major repair (>8 months)')
]
COST_OF_REPAIR = [
    ('Negligible or less than 5% of capital cost - score=1', 'Negligible or less than 5% of capital cost'),
    ('5-10% of capital cost - score=2', '5-10% of capital cost'),
    ('10-50% of capital cost - score=3', '10-50% of capital cost'),
    ('>50% of capital cost (new tank) - score=4', '>50% of capital cost (new tank)')
]
PROBABLE_MAGNITUDE_OF_PRODUCT_LOSS = [
    ('No release of product - score=1', 'No release of product'),
    ('<5% of tank contents - score=2', '<5% of tank contents'),
    ('>5% of tank contents - score=3', '>5% of tank contents')
]



LIKELIHOOD_OF_INJURY_TO_PERSONNEL = [
    ('No injury or near miss - score=1', 'No injury or near miss'),
    ('Minor injury - score=2', 'Minor injury'),
    ('Lost time injury/Medical treatment - score=3', 'Lost time injury/Medical treatment'),
    ('Serious injury/fatality on site - score=4', 'Serious injury/fatality on site')
]
PRODUCT_FLAMMABILITY_AS_PER_MCSP = [
    ('Class III(1) and unclassified product - score=1', 'Class III(1) and unclassified product'),
    ('Class II(1) product - score=2', 'Class II(1) product'),
    ('Class II(2) and III(2) product - score=3', 'Class II(2) and III(2) product'),
    ('Class I product - score=4', 'Class I product'),
]
PRODUCT_TOXICITY = [
    ('Non-toxic substances - score=1', 'Non-toxic substances'),
    ('Toxic substance if in contact with other substances - score=2', 'Toxic substance if in contact with other substances'),
    ('Toxic substance - score=3', 'Toxic substance'),
    ('Extremely toxic substance - score=4', 'Extremely toxic substance')
]
LOCATION_OF_TANK_FARM = [
    ('Tank farm within an abandonned area - score=1', 'Tank farm within an abandonned area'),
    ('Flat tank farm - score=2', 'Flat tank farm'),
    ('Flopping tank farm - score=3', 'Flopping tank farm'),
    ('In plant area within populous area - score=4', 'In plant area within populous area')
]
CONTINUED_LOCATION_OF_TANK_FARM = [
    ('No public fence near tank farm', 'No public fence near tank farm'),
    ('Presence of public fence near tank farm', 'Presence of public fence near tank farm')
]





# Environmental Aspects
ENVIRONMETAL_HAZARD_TO_SOIL_AND_WATER_AS_THE_POTENTIAL_TO_CAUSE = [
    ('No or negligle environment effect', 'No or negligle environment effect'),
    ('Environmental nuisance affecting neighbourhood', 'Environmental nuisance affecting neighbourhood'),
    ('Environmental pollution/Extensive restoration required', 'Environmental pollution/Extensive restoration required'),
    ('Severe demage/nuisance/pollution over large area', 'Severe demage/nuisance/pollution over large area')
]
VAPOUR_EMISSION = [
    ('No or negligle harmful (toxic) release', 'No or negligle harmful (toxic) release'),
    ('Small harmful (toxic) release', 'Small harmful (toxic) release'),
    ('Large (>1000m3) harmful (toxic) release', 'Large (>1000m3) harmful (toxic) release')
]



NDT_METHOD_USED_FOR_THICKNESS_MEASUREMENTS = [
    ('Crawler/beetle + US', 'Crawler /beetle + US'),
    ('US on gridline system', 'US on gridline system'),
    ('Visual + Spot ultrasonic (US)', 'Visual + Spot ultrasonic (US)')
]
FREQUENCY_OF_INTERNAL_INSPECTIONS_PERFORMED_DURING_SERVICE_LIFE = [
    ('Multiple inspections carried out', 'Multiple inspections carried out'),
    ('No or minimal inspection data available', 'No or minimal inspection data available')
]
CORROSION_ON_WIND_GIRDERS = [
    ('No corrosion on wind girders', 'No corrosion on wind girders'),
    ('Corrosion present but no effect on the integrity of tankk sheel plates', 'Corrosion present but no effect on the integrity of tankk shell plates'),
    ('Corrosion present and induces effect on integrity of tank sheel plates', 'Corrosion present and induces effect on integrity of tank shell plates')
]
BUCKLES_IN_SHELL_PLATES = [
    ('No buckles on tank shell plates', 'No buckles on tank shell plates'),
    ('Buckles present but no effect on the integrity of tank shell plates', 'Buckles present but no effect on the integrity of tank shell plates'),
    ('Buckles present and induces effect on integrity of tank sheel plates', 'Buckles present and induces effect on integrity of tank shell plates')
]
DIFFERENTIAL_SETLLEMENT_BETWEEN_TANK_STRUCTURE_AND_PIPING_SUPPORT = [
    ('No moments in shell nozzles or structures available which reduce nozzle loads', 'No moments in shell nozzles or structures available which reduce nozzle loads'),
    ('Moments present, but no effect on integrity of tank shell plates', 'Moments present, but no effect on integrity of tank shell plates'),
    ('Moments present and they induce effects on integrity of tank shell plates', 'Moments present and they induce effects on integrity of tank shell plates')
]









