from django.db import models

from bottom_plates.INPUT_FIELDS_SELECTION import *



class ImpressCathodicProtection(models.Model):
    name = models.CharField(max_length=100,
            choices=IMPRE_CATHODIC_PROTECTION,
            default='All readings around the periphery > 0.85 V - Score=0',
            verbose_name='1: Impressed cathodic protection'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Impressed cathodic protection'
        verbose_name_plural = 'Impressed cathodic protection'



class SacrificialCathodicPropection(models.Model):
    name = models.CharField(max_length=100,
            choices=SACRIFICIAL_CATHODIC_PROPECTION,
            default='Sacrificial CP available and operating - Score=0',
            verbose_name='1: Impressed cathodic protection'
    )

    def __str__(self):
        return self.name



class BottomPlatesInternalCoatingLining(models.Model):
    name = models.CharField(max_length=100,
            choices=BOTTOM_PLATES_INTERNAL_COATING_OR_LINING,
            default='Internal coating applied and quality is sound - Score=0',
            verbose_name='3: Bottom plates internal coating or lining'
    )

    def __str__(self):
        return self.name



class BottomPlatesExternalCoating(models.Model):
    name = models.CharField(max_length=100,
            choices=BOTTOM_PLATES_EXTERNAL_COATING,
            default='Internal coating applied and quality is sound - Score=0',
            verbose_name='4: Bottom plates internal coating (other than shop primer)'
    )

    def __str__(self):
        return self.name


DEGREE_SIGN = u'\N{DEGREE SIGN}'

class StorageConditions(models.Model):
    name = models.CharField(max_length=100,
            choices=STORAGE_CONDITIONS,
            default=f'Temperature of product < 40{DEGREE_SIGN}C - Score=0',
            verbose_name='5a: Type of bottom'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Storage Condition'
        verbose_name_plural = 'Storage Conditions'



class TypeOfBottom(models.Model):
    name = models.CharField(max_length=100,
            choices=TYPE_OF_BOTTOM,
            default='Cone up - Score=0',
            verbose_name='5b: Type of bottom'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type Of Bottom'
        verbose_name_plural = 'Types Of Bottom'



class HeatingCoilsInTank(models.Model):
    name = models.CharField(max_length=100,
            choices=HEATING_COILS_IN_TANK,
            default='No heating coil or no contact between heating coil and bottom plates - Score=0',
            verbose_name='5c: Heating coils in tank'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Heating Coils In Tank'
        verbose_name_plural = 'Heating Coils In Tank'


class ProductCorrosivity(models.Model):
    name = models.CharField(max_length=330,
            choices=PRODUCT_CORROSIVITY,
            default='Group 1/Risk H - Score=2',
            verbose_name='6: Product Corrosivity')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Corrosivity'
        verbose_name_plural = 'Product Corrosivity'



class FoundationType(models.Model):
    name = models.CharField(max_length=330,
            choices=FOUNDATION_TYPE,
            default='Piled concrete raft - Score=0',
            verbose_name='7: Foundation type'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Foundation Type'
        verbose_name_plural = 'Foundation Type'



class HeightOfFoundation(models.Model):
    name = models.CharField(max_length=100,
            choices=HEIGHT_OF_FOUNDATION,
            default='Tank bottom free from contact with water - Score=0',
            verbose_name='8: Height of foundation')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Height Of Foundation'
        verbose_name_plural = 'Height Of Foundation'


class EffectivenessOfDrainage(models.Model):
    name = models.CharField(max_length=150,
            choices=EFFECTIVENESS_OF_DRAINAGE,
            default='Slope of tank pad shoulder allows for adequate drainage away from tank bottom - Score=0',
            verbose_name='9: Effectiveness of drainage')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Effectiveness Of Drainage'
        verbose_name_plural = 'Effectiveness Of Drainage'



class TimeToRepair(models.Model):
    name = models.CharField(max_length=100,
            choices=TIME_TO_REPAIR,
            default='No internal entry required limited repair, no limitation on repair time - Score=1',
            verbose_name='10a: Time to repair'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Time To Repair'
        verbose_name_plural = 'Time To Repair'



class CostOfRepair(models.Model):
    name = models.CharField(max_length=100,
            choices=COST_OF_REPAIR,
            default='Negligible or less than 5% of capital cost - Score=1',
            verbose_name='10b: Cost of repair'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cost Of Repair'
        verbose_name_plural = 'Cost Of Repair'



class ProbableMagnitudeOfProductLoss(models.Model):
    name = models.CharField(max_length=100,
            choices=PROBABLE_MAGNITUDE_OF_PRODUCT_LOSS,
            default='No release of product - Score=1',
            verbose_name='10c: Probable magnitude of product loss'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Probable Magnitude Of ProductLoss'
        verbose_name_plural = 'Probable Magnitude Of Product Loss'



class LikelihoodOfInjuryToPersonnel(models.Model):
    name = models.CharField(max_length=100,
            choices=LIKELIHOOD_OF_INJURY_TO_PERSONNEL,
            default='No injury or near miss - Score=1',
            verbose_name='12a: Likelihood of injury to personnel'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Likelihood Of Injury To Personnel'
        verbose_name_plural = 'Likelihood Of Injury To Personnel'



class ProductFlammabilityAsPerMCSP(models.Model):
    name = models.CharField(max_length=100,
            choices=PRODUCT_FLAMMABILITY_AS_PER_MCSP,
            default='Class III(1) and unclassified product - Score=1',
            verbose_name='12b: Product flammability as per MCSP'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Flammability As Per MCSP'
        verbose_name_plural = 'Product Flammability As Per MCSP'




class ProductToxicity(models.Model):
    name = models.CharField(max_length=100,
            choices=PRODUCT_TOXICITY,
            default='Non-toxic substances- Score=1',
            verbose_name='12c: Product toxicity'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Toxicity'
        verbose_name_plural = 'Product Toxicity'



class LocationOfTankFarm(models.Model):
    name = models.CharField(max_length=100,
            choices=LOCATION_OF_TANK_FARM,
            default='Tank farm within an abandonned area - Score=1',
            verbose_name='12d: Location of tank farm')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location Of Tank Farm'
        verbose_name_plural = 'Location Of Tank Farm'


class TankLocatedNearPublicFence(models.Model):
    name = models.CharField(max_length=100,
            choices=TANK_LOCATED_NEAR_A_PUBLIC_FENCE,
            default='No - Score=0',
            verbose_name='12d: Location of tank farm')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tank Located Near Public Fence'
        verbose_name_plural = 'Tank Located Near Public Fence'



class EnvironmetalHazardToSoilAndWater(models.Model):
    name = models.CharField(max_length=100,
            choices=ENVIRONMETAL_HAZARD_TO_SOIL_AND_WATER_AS_THE_POTENTIAL_TO_CAUSE,
            default='Nor or negligle environment effect - Score=1',
            verbose_name='14a: Environmetal hazard to soil and water as the potential to cause'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Environmetal Hazard To Soil And Water'
        verbose_name_plural = 'Environmetal Hazard To Soil And Water'



class VapourEmission(models.Model):
    name = models.CharField(max_length=100,
            choices=VAPOUR_EMISSION,
            default='No or negligle harmful (toxic) release - Score=1',
            verbose_name='14b: Vapour emission')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vapour Emission'
        verbose_name_plural = 'Vapour Emission'



class AccelerationFactorForPitting(models.Model):
    name = models.CharField(max_length=100,
            choices=ACCELERATION_FACTOR_FOR_PITTING,
            verbose_name='24. Acceleration factor for pitting',
            default='1.15'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Acceleration Factor For Pitting'
        verbose_name_plural = 'Acceleration Factor For Pitting'



class NDTMethodUsedForThicknessMeasurements(models.Model):
    name = models.CharField(max_length=100,
            choices=NDT_METHOD_USED_FOR_THICKNESS_MEASUREMENTS,
            default='Floor scan + US - Score=-0.1',
            verbose_name='28: NDT method used for thickness measurements'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1].split(')')[0])

    class Meta:
        verbose_name = 'NDT Method Used For Thickness Measurements'
        verbose_name_plural = 'NDT Method Used For Thickness Measurements'



class FrequencyOfInternalInspections(models.Model):
    name = models.CharField(max_length=100,
            choices=FREQUENCY_OF_INTERNAL_INSPECTIONS_PERFORMED_DURING_SERVICE_LIFE,
            default='Multiple inspections carried out - Score=0.1',
            verbose_name='29: Frequency of internal inspections performed during service life'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1])

    class Meta:
        verbose_name = 'Frequency Of Internal Inspections'
        verbose_name_plural = 'Frequency Of Internal Inspections'


class Ndt_Method_And_Qualification_Of_Ndt_Operators_In_Place_And_Assessed(models.Model):
    name = models.CharField(max_length=100,
            choices=NDT_METHOD_AND_QUALIFICATION_OF_NDT_OPERATORS_IN_PLACE_AND_ASSESSED,
            default='No - Score=0',
            verbose_name='Ndt Method And Qualification Of Ndt Operators In Place And Assessed'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1])

    class Meta:
        verbose_name = 'NDT Method And Qualification Of NDT Operators In Place And Assessed'
        verbose_name_plural = 'NDT Method And Qualification Of Ndt Operators In Place And Assessed'


class EvidenceAvailableOfCompletingPdca(models.Model):
    name = models.CharField(max_length=100,
            choices=IS_EVIDENCE_AVAILABLE_OF_COMPLETING_PDCA_CYCLE_ON_INSPECTION_ACTIVITIES,
            default='No - Score=0',
            verbose_name='Is Evidence Available Of Completing PDCA Cycle On Inspection Activities?'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1])

    class Meta:
        verbose_name = 'Is Evidence Available Of Completing PDCA Cycle On Inspection Activities'
        verbose_name_plural = 'Is Evidence Available Of Completing PDCA Cycle On Inspection Activities'



class DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeeds(models.Model):
    name = models.CharField(max_length=100,
            choices=DOES_THE_ORGANISATION_HAVE_THE_PROPER_QUALIFICATIONS_TO_DETERMINE_DEGRADATIONS_SPEEDS_AND_ASSESS_INSPECTION_RESULTS,
            default='No - Score=0',
            verbose_name='Does the Organisation Have the Proper Qualifications to Determine Degradations Speeds and Assess Inspection Results?'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1])

    class Meta:
        verbose_name = 'Does the Organisation Have the Proper Qualifications to Determine Degradations Speeds and Assess Inspection Results?'
        verbose_name_plural = 'Does the Organisation Have the Proper Qualifications to Determine Degradations Speeds and Assess Inspection Results?'


class AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeam(models.Model):
    name = models.CharField(max_length=100,
            choices=ARE_RESULTS_ALWAYS_DISCUSSED_IN_A_MULTIDISCIPLINARY_RBI_TEAM,
            default='No - Score=1',
            verbose_name='Are Results Always Discussed in a Multidisciplinary RBI Team?'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1])

    class Meta:
        verbose_name = 'Are Results Always Discussed in a Multidisciplinary RBI Team?'
        verbose_name_plural = 'Are Results Always Discussed in a Multidisciplinary RBI Team?'


class Aretrainingrequirementsforrbiteammembersconsistentlyused(models.Model):
    name = models.CharField(max_length=100,
            choices=ARE_TRAINING_REQUIREMENTS_FOR_RBI_TEAM_MEMBERS_CONSISTENTLY_USED,
            default='No - Score=1',
            verbose_name='Are Training Requirements for RBI Team Members Consistently Used?'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1])

    class Meta:
        verbose_name = 'Are Training Requirements for RBI Team Members Consistently Used?'
        verbose_name_plural = 'Are Training Requirements for RBI Team Members Consistently Used?'



class DoesTheItemEvaluationHaveSignificantPitting(models.Model):
    name = models.CharField(max_length=100,
            choices=DOES_THE_ITEM_EVALUATION_HAVE_SIGNIFICANT_PITTING,
            default='No - Score=1',
            verbose_name='Does the Item Evaluation Have Significant Pitting?'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1])

    class Meta:
        verbose_name = 'Does the Item Evaluation Have Significant Pitting?'
        verbose_name_plural = 'Does the Item Evaluation Have Significant Pitting?'


class CanTheDegradationMechanismBeRegardedAsLinear(models.Model):
    name = models.CharField(max_length=100,
            choices=CAN_THE_DEGRADATION_MECHANISM_BE_REGARDED_AS_LINEAR,
            default='No - Score=1',
            verbose_name='Can the Degradation Mechanism be Regarded as Linear?'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1])

    class Meta:
        verbose_name = 'Can the Degradation Mechanism be Regarded as Linear?'
        verbose_name_plural = 'Can the Degradation Mechanism be Regarded as Linear?'



class IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration(models.Model):
    name = models.CharField(max_length=100,
            choices=IS_THE_CONSTRUCTION_SUCH_THAT_CORROSION_MAY_BE_REDUCED_BY_THE_CHOSEN_WELD_CONFIGURATION,
            default='No - Score=1',
            verbose_name='Is the Construction such that Corrosion may be Reduced by the Chosen Weld Configuration?'
    )

    def __str__(self):
        return self.name

    def score(self):
        return float(self.name.split('Score=')[1])

    class Meta:
        verbose_name = 'Is the Construction such that Corrosion may be Reduced by the Chosen Weld Configuration?'
        verbose_name_plural = 'Is the Construction such that Corrosion may be Reduced by the Chosen Weld Configuration?'


# class TypeOfInterconnectingBottomPlateWelds(models.Model):
#     name = models.CharField(max_length=100,
#             choices=IS_THE_CONSTRUCTION_SUCH_THAT_CORROSION_MAY_BE_REDUCED_BY_THE_CHOSEN_WELD_CONFIGURATION,
#             default='Butt welds - Score=0.1',
#             verbose_name='30: Type of interconnecting bottom plate welds outside of annular section'
#     )

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Type Of Interconnecting Bottom Plate Welds'
#         verbose_name_plural = 'Type Of Interconnecting Bottom Plate Welds'



class AreProceduresInPlaceToPreventWaterContact(models.Model):
    name = models.CharField(max_length=350,
            choices=ARE_PROCEDURES_IN_PLACE_TO_PREVENT_WATER_CONTACT,
            default='Yes - Score=1')
            # verbose_name='Are Procedures In Place To Prevent Water Contact')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Are Procedures In Place To Prevent Water Contact'
        verbose_name_plural = 'Are Procedures In Place To Prevent Water Contact'

class IsTheCorrosionRateDeterminedWithAtLeast2Sources(models.Model):
    name = models.CharField(max_length=350,
            choices=IS_THE_CORROSION_RATE_DETERMINED_WITH_AT_LEAST_2_SOURCES,
            default='Yes - Score=1')
            # verbose_name='Is The Corrosion Rate Determined With At Least 2 Sources')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Is The Corrosion Rate Determined With At Least 2 Sources'
        verbose_name_plural = 'Is The Corrosion Rate Determined With At Least 2 Sources'

class IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints(models.Model):
    name = models.CharField(max_length=350,
            choices=IS_THE_DEGRADATION_SPEED_CALCULATED_BY_USING_AT_LEAST_3_MEASUREMENT_POINTS,
            default='Yes - Score=1')
            # verbose_name='Is The Degradation Speed Calculated By Using At Least 3 Measurement Points')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Is The Degradation Speed Calculated By Using At Least 3 Measurement Points'
        verbose_name_plural = 'Is The Degradation Speed Calculated By Using At Least 3 Measurement Points'

class WhichMethodIsUsed(models.Model):
    name = models.CharField(max_length=350,
            choices=WHICH_METHOD_IS_USED,
            default='Yes - Score=1')
            # verbose_name='Which Method Is Used')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Which Method Is Used'
        verbose_name_plural = 'Which Method Is Used'


