from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

from .models import Project
from .serializers import (
    ProjectSerializer,
    UserSerializer,
)

from bottom_plates.models import (
    ProbabilityFactorData,
    ConsequenceFactorData,
    InspectionData,
    Results
)

from selectfields.models import (
    ImpressCathodicProtection,
    SacrificialCathodicPropection,
    BottomPlatesInternalCoatingLining,
    BottomPlatesExternalCoating,
    StorageConditions,
    TypeOfBottom,
    HeatingCoilsInTank,
    ProductCorrosivity,
    FoundationType,
    HeightOfFoundation,
    EffectivenessOfDrainage,
    TimeToRepair,
    CostOfRepair,
    ProbableMagnitudeOfProductLoss,
    LikelihoodOfInjuryToPersonnel,
    ProductFlammabilityAsPerMCSP,
    ProductToxicity,
    LocationOfTankFarm,
    EnvironmetalHazardToSoilAndWater,
    VapourEmission,
    AccelerationFactorForPitting,
    NDTMethodUsedForThicknessMeasurements,
    FrequencyOfInternalInspections,
    Ndt_Method_And_Qualification_Of_Ndt_Operators_In_Place_And_Assessed,
    EvidenceAvailableOfCompletingPdca,
    DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeeds,
    AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeam,
    Aretrainingrequirementsforrbiteammembersconsistentlyused,
    DoesTheItemEvaluationHaveSignificantPitting,
    CanTheDegradationMechanismBeRegardedAsLinear,
    IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration,


    AreProceduresInPlaceToPreventWaterContact,
    IsTheCorrosionRateDeterminedWithAtLeast2Sources,
    IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints,
    WhichMethodIsUsed,
)

import json
from datetime import datetime


class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()



@require_POST
@csrf_exempt
def create_project(request):
    data = json.loads(request.body)
    print(data)
    start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
    end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
    project = Project.objects.create(
        name=data['name'],
        description=data['description'],
        start_date=start_date,
        end_date=end_date,
    )
    return JsonResponse({
        'message': 'Project created successfully'
    })


def get_consequence_rating(rating):
    result = ''
    if rating >= 3:
        result = 'High'
    elif rating < 3 and rating >= 2.5:
        result = 'Medium'
    elif rating < 2.5 and rating >= 2:
        result = 'Low'
    elif x < 2:
        results = 'Negligible'

    return result

def get_probability_rating(rating):
    result = ''
    if rating >= 3:
        result = 'High'
    elif rating < 3 and rating >= 2.5:
        result = 'Medium'
    elif rating < 2.5 and rating >= 2.15:
        result = 'Low'
    elif rating < 2.15:
        result = 'Negligible'

    return result


def filtering_function(data, name):
    try:
        filtering = data[name]['name']
    except (TypeError, IndexError):
        filtering = data[name]
    return filtering


def update_field(func, data, keyValue, model):
    filtering = func(data, keyValue)
    sacrificial_cathodic_propect = model.objects.filter(name__icontains=filtering)
    if sacrificial_cathodic_propect.exists():
        first = sacrificial_cathodic_propect.first()
        return first
    return ''


def get_overall_score(score1, score2, score3):
    return max(score1, score2, score3)


def get_overall_rating(score1, score2, score3):
    scores = {
        'High': 4,
        'Medium': 3,
        'Low': 2,
        'Negligible': 1
    }
    values = {}
    values[score1] = scores[score1]
    values[score2] = scores[score2]
    values[score3] = scores[score3]
    highest = 0
    for key, val in values.items():
        if val > highest:
            highest = val

    return [key for key, value in scores.items() if value == highest][0]


def determine_matrix(probability_rating,
                     overall_consequence_rating):
    data = {}
    if (probability_rating == 'High' and
        overall_consequence_rating == 'High'):
        data['key'] = 'high-high'
        data['value'] = 'Extreme'
    elif (probability_rating == 'High' and
        overall_consequence_rating == 'Medium'):
        data['key'] = 'high-medium'
        data['value'] = 'Extreme'
    elif (probability_rating == 'Medium' and
        overall_consequence_rating == 'High'):
        data['key'] = 'medium-high'
        data['value'] = 'Extreme'

    elif (probability_rating == 'High' and
        overall_consequence_rating == 'Low'):
        data['key'] = 'high-low'
        data['value'] = 'High'
    elif (probability_rating == 'Medium' and
        overall_consequence_rating == 'Medium'):
        data['key'] = 'medium-medium'
        data['value'] = 'High'
    elif (probability_rating == 'Low' and
        overall_consequence_rating == 'High'):
        data['key'] = 'low-high'
        data['value'] = 'High'

    elif (probability_rating == 'High' and
        overall_consequence_rating == 'Negligible'):
        data['key'] = 'high-negligible'
        data['value'] = 'Low'
    elif (probability_rating == 'Medium' and
        overall_consequence_rating == 'Negligible'):
        data['key'] = 'medium-negligible'
        data['value'] = 'Low'
    elif (probability_rating == 'Low' and
        overall_consequence_rating == 'Low'):
        data['key'] = 'low-low'
        data['value'] = 'Low'
    elif (probability_rating == 'Negligible' and
        overall_consequence_rating == 'Medium'):
        data['key'] = 'negligible-medium'
        data['value'] = 'Low'


    elif (probability_rating == 'Medium' and
        overall_consequence_rating == 'Low'):
        data['key'] = 'medium-low'
        data['value'] = 'Medium'
    elif (probability_rating == 'Low' and
        overall_consequence_rating == 'Medium'):
        data['key'] = 'low-medium'
        data['value'] = 'Medium'
    elif (probability_rating == 'Negligible' and
        overall_consequence_rating == 'High'):
        data['key'] = 'negligible-high'
        data['value'] = 'Medium'

    elif (probability_rating == 'Low' and
        overall_consequence_rating == 'Negligible'):
        data['key'] = 'low-negligible'
        data['value'] = 'Negligible'
    elif (probability_rating == 'Negligible' and
        overall_consequence_rating == 'Negligible'):
        data['key'] = 'negligible-negligible'
        data['value'] = 'Negligible'
    elif (probability_rating == 'Negligible' and
        overall_consequence_rating == 'Low'):
        data['key'] = 'negligible-low'
        data['value'] = 'Negligible'

    return data



def k_initial_matrix(probability_rating,
                     consequence_rating):
    k_initial = None

    if ((probability_rating == 'Low' and consequence_rating == 'Negligible') or
        (probability_rating == 'Negligible' and consequence_rating == 'Negligible') or
        (probability_rating == 'Negligible' and consequence_rating == 'Low')):
        k_initial = 0.9
    elif ((probability_rating == 'High' and consequence_rating == 'Negligible') or
          (probability_rating == 'Medium' and consequence_rating == 'Negligible') or
          (probability_rating == 'Low' and consequence_rating == 'Low') or
          (probability_rating == 'Negligible' and consequence_rating == 'Medium')):
        k_initial = 0.8
    elif ((probability_rating == 'Medium' and consequence_rating == 'Low') or
          (probability_rating == 'Low' and consequence_rating == 'Medium') or
          (probability_rating == 'Negligible' and consequence_rating == 'High')):
        k_initial = 0.7
    elif ((probability_rating == 'High' and consequence_rating == 'Low') or
          (probability_rating == 'Medium' and consequence_rating == 'Medium') or
          (probability_rating == 'Low' and consequence_rating == 'High')):
        k_initial = 0.6
    elif ((probability_rating == 'High' and consequence_rating == 'Medium') or
          (probability_rating == 'High' and consequence_rating == 'High') or
          (probability_rating == 'Medium' and consequence_rating == 'High')):
        k_initial = 0.5

    return k_initial



def extract_score_yn(name):
    return name.split('=')[1]

@require_POST
@csrf_exempt
def update_project_details(request):
    data = json.loads(request.body)
    project = Project.objects.filter(id=data['id'])
    proj = None
    message = None
    print('\n', data, '\n')
    print('*' * 100)

    if project.exists():
        proj = project.first()
        message = "Project exists."
        probability_factor_data = ProbabilityFactorData.objects.get(id=proj.default_values.probability_factor_data.id)

        impresses_cathodic_protect = update_field(filtering_function, data, 'impressCathodProtectionValue', ImpressCathodicProtection)
        probability_factor_data.impresses_cathodic_protect = impresses_cathodic_protect
        impresses_cathodic_protect_score = float(impresses_cathodic_protect.name.split(' - ')[-1].split('=')[-1])
        print('\nimpresses_cathodic_protect_score = ', impresses_cathodic_protect_score, '\n')

        sacrificial_cathodic_propect = update_field(filtering_function, data, 'sacriCathProteValue', SacrificialCathodicPropection)
        probability_factor_data.sacrificial_cathodic_propect = sacrificial_cathodic_propect
        sacrificial_cathodic_propect_score = float(sacrificial_cathodic_propect.name.split(' - ')[-1].split('=')[-1])
        print('\nsacrificial_cathodic_propect_score = ', sacrificial_cathodic_propect_score, '\n')

        bottom_plates_internal_coating_or_linin = update_field(filtering_function, data, 'bottomPlatesInternalCoatingValue', BottomPlatesInternalCoatingLining)
        probability_factor_data.bottom_plates_internal_coating_or_linin = bottom_plates_internal_coating_or_linin
        bottom_plates_internal_coating_or_linin_score = float(bottom_plates_internal_coating_or_linin.name.split(' - ')[-1].split('=')[-1])
        print('\nbottom_plates_internal_coating_or_linin_score = ', bottom_plates_internal_coating_or_linin_score, '\n')

        bottom_plates_external_coatin = update_field(filtering_function, data, 'bottomPlatesExternalCoatingValue', BottomPlatesExternalCoating)
        probability_factor_data.bottom_plates_external_coatin = bottom_plates_external_coatin
        bottom_plates_external_coatin_score = float(bottom_plates_external_coatin.name.split(' - ')[-1].split('=')[-1])
        print('\nbottom_plates_external_coatin_score = ', bottom_plates_external_coatin_score, '\n')

        storage_condition = update_field(filtering_function, data, 'storageConditionValue', StorageConditions)
        probability_factor_data.storage_condition = storage_condition
        storage_condition_score = float(storage_condition.name.split(' - ')[-1].split('=')[-1])
        print('\nstorage_condition_score = ', storage_condition_score, '\n')

        types_of_bottom = update_field(filtering_function, data, 'typeOfBottonValue', TypeOfBottom)
        probability_factor_data.types_of_bottom = types_of_bottom
        types_of_bottom_score = float(types_of_bottom.name.split(' - ')[-1].split('=')[-1])
        print('\ntypes_of_bottom_score = ', types_of_bottom_score, '\n')

        heating_coils_in_tanks = update_field(filtering_function, data, 'heatingCoilsInTankValue', HeatingCoilsInTank)
        probability_factor_data.heating_coils_in_tanks = heating_coils_in_tanks
        heating_coils_in_tanks_score = float(heating_coils_in_tanks.name.split(' - ')[-1].split('=')[-1])
        print('\nheating_coils_in_tanks_score = ', heating_coils_in_tanks_score, '\n')


        weighted_score_5 = (storage_condition_score +
                          types_of_bottom_score +
                          heating_coils_in_tanks_score) / 2.5
        print(f'------------------------->')
        print(f'weighted_score_5 = {weighted_score_5}')
        print(f'<-------------------------')


        products_corrosivity = update_field(filtering_function, data, 'productCorrosivityValue', ProductCorrosivity)
        probability_factor_data.products_corrosivity = products_corrosivity
        products_corrosivity_score = float(products_corrosivity.name.split(' - ')[-1].split('=')[-1])
        print('\nproducts_corrosivity_score = ', products_corrosivity_score, '\n')

        foundation_types = update_field(filtering_function, data, 'foundationTypeValue', FoundationType)
        probability_factor_data.foundation_types = foundation_types
        foundation_types_score = float(foundation_types.name.split(' - ')[-1].split('=')[-1])
        print('\nfoundation_types_score = ', foundation_types_score, '\n')

        heights_of_foundation = update_field(filtering_function, data, 'heightOfFoundationValue', HeightOfFoundation)
        probability_factor_data.heights_of_foundation = heights_of_foundation
        heights_of_foundation_score = float(heights_of_foundation.name.split(' - ')[-1].split('=')[-1])
        print('\nheights_of_foundation_score = ', heights_of_foundation_score, '\n')

        effectiveness_of_drainages = update_field(filtering_function, data, 'effectiveDrainageValue', EffectivenessOfDrainage)
        probability_factor_data.effectiveness_of_drainages = effectiveness_of_drainages
        effectiveness_of_drainages_score = float(effectiveness_of_drainages.name.split(' - ')[-1].split('=')[-1])
        print('\neffectiveness_of_drainages_score = ', effectiveness_of_drainages_score, '\n')

        probability_factor = ((2 * impresses_cathodic_protect_score) +
                              (1 * sacrificial_cathodic_propect_score) +
                              (3 * bottom_plates_internal_coating_or_linin_score) +
                              (2 * bottom_plates_external_coatin_score) +
                              (2 * weighted_score_5) +
                              (4 * products_corrosivity_score) +
                              (5 * foundation_types_score) +
                              (2 * heights_of_foundation_score) +
                              (3 * effectiveness_of_drainages_score)) / 9
        print(f'probability_factor = {probability_factor}')
        probability_rating = get_probability_rating(probability_factor)
        probability_factor = str(probability_factor)[:5]
        # print(f'probability_factor = {probability_factor}')
        print(f'probability_rating = {probability_rating}')

        probability_factor_data.save()




        consequence_factor_data = ConsequenceFactorData.objects.get(id=proj.default_values.consequence_factor_data.id)

        time_to_repair = update_field(filtering_function, data, 'timeToRepairValue', TimeToRepair)
        consequence_factor_data.time_to_repair = time_to_repair
        time_to_repair_score = float(time_to_repair.name.split(' - ')[-1].split('=')[-1])
        print('\ntime_to_repair_score = ', time_to_repair_score, '\n')

        cost_of_repair = update_field(filtering_function, data, 'costOfRepairValue', CostOfRepair)
        consequence_factor_data.cost_of_repair = cost_of_repair
        cost_of_repair_score = float(cost_of_repair.name.split(' - ')[-1].split('=')[-1])
        print('\ncost_of_repair_score = ', cost_of_repair_score, '\n')

        probable_magnitude_of_product_loss = update_field(filtering_function, data, 'drainageMagnitudeValue', ProbableMagnitudeOfProductLoss)
        consequence_factor_data.probable_magnitude_of_product_loss = probable_magnitude_of_product_loss
        probable_magnitude_of_product_loss_score = float(probable_magnitude_of_product_loss.name.split(' - ')[-1].split('=')[-1])
        print('\nprobable_magnitude_of_product_loss_score = ', probable_magnitude_of_product_loss_score, '\n')

        first_value = (time_to_repair_score +
                       cost_of_repair_score) / 2
        economic_aspects_consequence_factor = max(first_value,
                                                  probable_magnitude_of_product_loss_score)
        print(f'------------------------->')
        print(f'economic_aspects_consequence_factor = {economic_aspects_consequence_factor}')
        print(f'<-------------------------')
        economic_aspects_consequence_rating = get_consequence_rating(economic_aspects_consequence_factor)


        likelihood_of_injury_to_personnel = update_field(filtering_function, data, 'likelihoodOfInjuryValue', LikelihoodOfInjuryToPersonnel)
        consequence_factor_data.likelihood_of_injury_to_personnel = likelihood_of_injury_to_personnel
        likelihood_of_injury_to_personnel_score = float(likelihood_of_injury_to_personnel.name.split(' - ')[-1].split('=')[-1])
        print('\nlikelihood_of_injury_to_personnel_score = ', likelihood_of_injury_to_personnel_score, '\n')

        product_flammability_as_per_MCSP = update_field(filtering_function, data, 'productFlamabilityValue', ProductFlammabilityAsPerMCSP)
        consequence_factor_data.product_flammability_as_per_MCSP = product_flammability_as_per_MCSP
        product_flammability_as_per_MCSP_score = float(product_flammability_as_per_MCSP.name.split(' - ')[-1].split('=')[-1])
        print('\nproduct_flammability_as_per_MCSP_score = ', product_flammability_as_per_MCSP_score, '\n')

        if data["productToxicityValue"] == "Non-toxic substance":
            product_toxicity_name = ProductToxicity.objects.get(id=1)
        elif data["productToxicityValue"] == "Toxic substance":
            product_toxicity_name = ProductToxicity.objects.get(id=3)
        else:
            product_toxicity_name = update_field(filtering_function, data, 'productToxicityValue', ProductToxicity)

        # print(f'product_toxicity_name = {product_toxicity_name}')
        consequence_factor_data.product_toxicity = product_toxicity_name
        product_toxicity_score = float(product_toxicity_name.name.split('- ')[-1].split('=')[-1])
        print('product_toxicity_score = ', product_toxicity_score, '\n')

        location_of_tank_farm = update_field(filtering_function, data, 'locationOfTankValue', LocationOfTankFarm)
        consequence_factor_data.location_of_tank_farm = location_of_tank_farm
        location_of_tank_farm_score = float(location_of_tank_farm.name.split(' - ')[-1].split('=')[-1])
        print('\nlocation_of_tank_farm_score = ', location_of_tank_farm_score, '\n')

        # tank_located_near_public_fence_value = update_field(filtering_function, data, 'tankLocatedNearPublicFenceValue', LocationOfTankFarm)
        tank_located_near_public_fence_value = data.get('tankLocatedNearPublicFenceValue')
        tank_located_near_public_fence_value_score = 1 if tank_located_near_public_fence_value == 'Yes' else 0
        print(f'tank_located_near_public_fence_value = {tank_located_near_public_fence_value_score}')

        first_value = (product_flammability_as_per_MCSP_score +
                       product_toxicity_score +
                       location_of_tank_farm_score +
                       tank_located_near_public_fence_value_score) / 3
        health_and_safety_aspects_consequence_factor = max(first_value,
                     likelihood_of_injury_to_personnel_score)
        print(f'------------------------->')
        print(f'health_and_safety_aspects_consequence_factor = {health_and_safety_aspects_consequence_factor}')
        print(f'<-------------------------')
        health_and_safety_aspects_consequence_rating = get_consequence_rating(health_and_safety_aspects_consequence_factor)


        environmetal_hazard = update_field(filtering_function, data, 'environHazardValue', EnvironmetalHazardToSoilAndWater)
        consequence_factor_data.environmetal_hazard_to_soil_and_water_as_the_potential_to_cause = environmetal_hazard
        environmetal_hazard_score = float(environmetal_hazard.name.split(' - ')[-1].split('=')[-1])
        print('\nenvironmetal_hazard_score = ', environmetal_hazard_score, '\n')

        vapour_emission = update_field(filtering_function, data, 'vapourEmissionValue', VapourEmission)
        consequence_factor_data.vapour_emission = vapour_emission
        vapour_emission_score = float(vapour_emission.name.split(' - ')[-1].split('=')[-1])
        print('\nvapour_emission_score = ', vapour_emission_score, '\n')

        environmental_aspects_consequence_factor = max(environmetal_hazard_score,
                     vapour_emission_score)
        print(f'------------------------->')
        print(f'environmental_aspects_consequence_factor = {environmental_aspects_consequence_factor}')
        print(f'<-------------------------')
        environmental_aspects_consequence_rating = get_consequence_rating(environmental_aspects_consequence_factor)

        consequence_factor_data.save()

        overall_consequence_rating = get_overall_rating(economic_aspects_consequence_rating,
                                              health_and_safety_aspects_consequence_rating,
                                              environmental_aspects_consequence_rating)
        overall_consequence_factor = get_overall_score(economic_aspects_consequence_factor,
                                              health_and_safety_aspects_consequence_factor,
                                              environmental_aspects_consequence_factor)

        print(f'''overall_consequence_rating = {overall_consequence_rating}''')
        print(f'''overall_consequence_factor = {overall_consequence_factor}''')


        inspection_data = InspectionData.objects.get(id=proj.default_values.inspection_data.id)

        last_inspection = data['lastInspectionValue']
        inspection_data.last_inspection = datetime.strptime(last_inspection, '%Y-%m-%d').date()
        print('\nlast_inspection = ', last_inspection, '\n')

        minimum_thickness_measured_during_previous_inspection = data['minThicknessMeasuredPrevInspValue']
        inspection_data.minimum_thickness_measured_during_previous_inspection = minimum_thickness_measured_during_previous_inspection
        print('\nminimum_thickness_measured_during_previous_inspection = ', minimum_thickness_measured_during_previous_inspection, '\n')

        period_of_service_between_previous_inspection_and_this_inspection = data['periodOfServiceBetweenPrevAndPresentInspeValue']
        inspection_data.period_of_service_between_previous_inspection_and_this_inspection = period_of_service_between_previous_inspection_and_this_inspection
        # period_of_service_between_previous_inspection_and_this_inspection_score = int(period_of_service_between_previous_inspection_and_this_inspection.name.split(' - ')[-1].split('=')[-1])
        print('\nperiod_of_service_between_previous_inspection_and_this_inspection = ', period_of_service_between_previous_inspection_and_this_inspection, '\n')

        minimum_thickness_measured_during_present_inspection = data['minThicknessMeasuredPresentInspValue']
        inspection_data.minimum_thickness_measured_during_present_inspection = minimum_thickness_measured_during_present_inspection
        print('\nminimum_thickness_measured_during_present_inspection = ', minimum_thickness_measured_during_present_inspection, '\n')

        minimum_allowable_bottom_place_thickness = data['minAllowBottomPlaceThicknessValue']
        inspection_data.minimum_allowable_bottom_place_thickness = minimum_allowable_bottom_place_thickness
        print('\nminimum_allowable_bottom_place_thickness = ', minimum_allowable_bottom_place_thickness, '\n')

        try:
            corrosion_rate = ((float(minimum_thickness_measured_during_previous_inspection) -
                            float(minimum_thickness_measured_during_present_inspection)) /
                            float(period_of_service_between_previous_inspection_and_this_inspection))
            corrosion_rate = round(corrosion_rate, 3)
        except ValueError:
            corrosion_rate = float(data['averageCorrosionRate'])

        print(f'------------------------->')
        print(f'corrosion_rate = {corrosion_rate}')
        print(f'<-------------------------')

        acceleration_factor_for_pitting = update_field(filtering_function, data, 'accelerationFactorForPittingValue', AccelerationFactorForPitting)
        inspection_data.acceleration_factor_for_pitting = acceleration_factor_for_pitting
        acceleration_factor_for_pitting_score = float(acceleration_factor_for_pitting.name.split(' - ')[-1].split('=')[-1])
        print('\nacceleration_factor_for_pitting_score = ', acceleration_factor_for_pitting_score, '\n')

        adjusted_corrosion_rate = (corrosion_rate * acceleration_factor_for_pitting_score)
        print(f'------------------------->')
        print(f'adjusted_corrosion_rate = {adjusted_corrosion_rate}')
        print(f'<-------------------------')

        remaining_life = (float(minimum_thickness_measured_during_present_inspection) -
                          float(minimum_allowable_bottom_place_thickness)) / adjusted_corrosion_rate
        remaining_life = round(remaining_life, 3)
        print(f'remaining_life = {remaining_life}')


        # Corrosion Rate Assessment
        print('\nCORROSION RATE ASSESSMENT')
        procedures_in_place_value = AreProceduresInPlaceToPreventWaterContact.objects.get(name__icontains=data['proceduresInPlaceValue'])
        procedures_in_place_value_score = extract_score_yn(procedures_in_place_value.name)
        print(f'procedures_in_place_value_score = {procedures_in_place_value_score}')

        is_corrosion_rate_determined_value = IsTheCorrosionRateDeterminedWithAtLeast2Sources.objects.get(name__icontains=data['isCorrosionRateDeterminedValue'])
        is_corrosion_rate_determined_score = extract_score_yn(is_corrosion_rate_determined_value.name)
        print(f'is_corrosion_rate_determined_score = {is_corrosion_rate_determined_score}')

        is_degradation_speed_calculated_value = IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints.objects.get(name__icontains=data['isDegradationSpeedCalculatedValue'])
        is_degradation_speed_calculated_score = extract_score_yn(is_degradation_speed_calculated_value.name)
        print(f'is_degradation_speed_calculated_score = {is_degradation_speed_calculated_score}')

        which_method_is_used_value = WhichMethodIsUsed.objects.get(name__icontains=data['whichMethodIsUsedValue'])
        which_method_is_used_score = extract_score_yn(which_method_is_used_value.name)
        print(f'which_method_is_used_score = {which_method_is_used_score}')

        weighted_factor_Kcr = (float(procedures_in_place_value_score) +
                               float(is_corrosion_rate_determined_score) +
                               float(is_degradation_speed_calculated_score) +
                               float(which_method_is_used_score)) / 4
        print(f'weighted_factor_Kcr = {weighted_factor_Kcr}\n')


        # Inspection Effectiveness
        print('INSPECTION EFFECTIVENESS')
        NDT_method_used_and_extent_of_coverage = NDTMethodUsedForThicknessMeasurements.objects.get(name__icontains=data['NDTMethodExtentCoverageValue'])
        NDT_method_used_and_extent_of_coverage_score = NDT_method_used_and_extent_of_coverage.score()
        print(f'NDT_method_used_and_extent_of_coverage_score = {NDT_method_used_and_extent_of_coverage_score}')

        frequency_of_internal_inspections_performed_during_service_life_of_tank = FrequencyOfInternalInspections.objects.get(name__icontains=data['FrequencyInternalInspectionsValue'])
        frequency_of_internal_inspections_performed_during_service_life_of_tank_score = frequency_of_internal_inspections_performed_during_service_life_of_tank.score()
        print(f'frequency_of_internal_inspections_performed_during_service_life_of_tank_score = {frequency_of_internal_inspections_performed_during_service_life_of_tank_score}')

        NDT_method_and_qualification_of_NDT_operators = Ndt_Method_And_Qualification_Of_Ndt_Operators_In_Place_And_Assessed.objects.get(name__icontains=data['NDTMethodQualificationValue'])
        NDT_method_and_qualification_of_NDT_operators_score = NDT_method_and_qualification_of_NDT_operators.score()
        print(f'NDT_method_and_qualification_of_NDT_operators_score = {NDT_method_and_qualification_of_NDT_operators_score}')


        weighted_factor_Kie = (float(procedures_in_place_value_score) +
                               float(frequency_of_internal_inspections_performed_during_service_life_of_tank_score) +
                               float(NDT_method_and_qualification_of_NDT_operators_score))  / 3
        print(f'weighted_factor_Kie = {weighted_factor_Kie}\n')


        # Maturity of the Assessment
        print('MATURITY OF THE ASSESSMENT')
        evidence_available_completing_PDCA = EvidenceAvailableOfCompletingPdca.objects.get(name__icontains=data['EvidenceAvailableCompletingPDCAValue'])
        evidence_available_completing_PDCA_score = evidence_available_completing_PDCA.score()
        print(f'evidence_available_completing_PDCA_score = {evidence_available_completing_PDCA_score}')

        organisation_have_proper_qualifications = DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeeds.objects.get(name__icontains=data['OrganisationHaveProperQualificationsValue'])
        organisation_have_proper_qualifications_score = organisation_have_proper_qualifications.score()
        print(f'organisation_have_proper_qualifications_score = {organisation_have_proper_qualifications_score}')

        are_results_always_discussed = AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeam.objects.get(name__icontains=data['AreResultsAlwaysDiscussedValue'])
        are_results_always_discussed_score = are_results_always_discussed.score()
        print(f'are_results_always_discussed_score = {are_results_always_discussed_score}')

        are_training_requirements = Aretrainingrequirementsforrbiteammembersconsistentlyused.objects.get(name__icontains=data['AreTrainingRequirementsValue'])
        are_training_requirements_score = are_training_requirements.score()
        print(f'are_training_requirements_score = {are_training_requirements_score}')

        weighted_factor_Kma = (float(evidence_available_completing_PDCA_score) +
                               float(organisation_have_proper_qualifications_score) +
                               float(are_results_always_discussed_score) +
                               float(are_training_requirements_score)) / 4
        print(f'weighted_factor_Kma = {weighted_factor_Kma}\n')


        # Predictability of the Mechanism
        print('\nPREDICTABILITY OF THE MECHANISM')
        item_evaluation_have_significant = DoesTheItemEvaluationHaveSignificantPitting.objects.get(name__icontains=data['ItemEvaluationHaveSignificantValue'])
        item_evaluation_have_significant_score = item_evaluation_have_significant.score()
        print(f'item_evaluation_have_significant_score = {item_evaluation_have_significant_score}')

        degradation_mechanism = CanTheDegradationMechanismBeRegardedAsLinear.objects.get(name__icontains=data['DegradationMechanismValue'])
        degradation_mechanism_score = degradation_mechanism.score()
        print(f'degradation_mechanism_score = {degradation_mechanism_score}')

        construction_such_corrosion = IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration.objects.get(name__icontains=data['ConstructionsuchCorrosionValue'])
        construction_such_corrosion_score = construction_such_corrosion.score()
        print(f'construction_such_corrosion_score = {construction_such_corrosion_score}')

        weighted_factor_Kpr = (float(item_evaluation_have_significant_score) +
                               float(degradation_mechanism_score) +
                               float(construction_such_corrosion_score)) / 3
        print(f'weighted_factor_Kpr = {weighted_factor_Kpr}\n')

        k_initial = k_initial_matrix(probability_rating,
                                     overall_consequence_rating)
        k_initial = round(k_initial, 3)
        print(f'k_initial = {k_initial}')

        k_conf_initial = (1 * weighted_factor_Kcr +
                          3 * weighted_factor_Kie +
                          2 * weighted_factor_Kma +
                          1 * weighted_factor_Kpr) / 7
        k_conf_initial = round(k_conf_initial, 3)
        print(f'k_conf_initial = {k_conf_initial}')

        k_conf = 0.4 * k_conf_initial - 0.2
        k_conf = round(k_conf, 3)
        print(f'k_conf = {k_conf}')

        k_final = k_conf - k_initial
        k_final = round(k_final, 3)
        print(f'k_final = {k_final}')

        interval_between_next_required_inspection = k_final * remaining_life
        print(f'interval_between_next_required_inspection = {interval_between_next_required_inspection}')


        NDT_method_used_for_thickness_measurements = update_field(filtering_function, data, 'ndtMethodUsedValue', NDTMethodUsedForThicknessMeasurements)
        inspection_data.NDT_method_used_for_thickness_measurements = NDT_method_used_for_thickness_measurements
        # NDT_method_used_for_thickness_measurements_score = float(NDT_method_used_for_thickness_measurements.name.split(' - ')[-1].split('=')[-1])
        print('\nNDT_method_used_for_thickness_measurements_score = ', NDT_method_used_for_thickness_measurements, '\n')

        frequency_of_internal_inspections_performed_during_service_life = update_field(filtering_function, data, 'freqOfInternalInspValue', FrequencyOfInternalInspections)
        inspection_data.frequency_of_internal_inspections_performed_during_service_life = frequency_of_internal_inspections_performed_during_service_life
        frequency_of_internal_inspections_performed_during_service_life_score = float(frequency_of_internal_inspections_performed_during_service_life.name.split(' - ')[-1].split('=')[-1])
        print('\nfrequency_of_internal_inspections_performed_during_service_life_score = ', frequency_of_internal_inspections_performed_during_service_life_score, '\n')

        Is_the_Construction_such_that_Corrosion_may_be_Reduced_by_the_Chosen_Weld_Configuration = update_field(filtering_function, data, 'ConstructionsuchCorrosionValue', IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration)
        inspection_data.Is_the_Construction_such_that_Corrosion_may_be_Reduced_by_the_Chosen_Weld_Configuration = Is_the_Construction_such_that_Corrosion_may_be_Reduced_by_the_Chosen_Weld_Configuration
        type_of_interconnecting_bottom_plate_welds_outside_of_annular_section_score = float(Is_the_Construction_such_that_Corrosion_may_be_Reduced_by_the_Chosen_Weld_Configuration.name.split(' - ')[-1].split('=')[-1])
        print('\ntype_of_interconnecting_bottom_plate_welds_outside_of_annular_section_score = ', type_of_interconnecting_bottom_plate_welds_outside_of_annular_section_score, '\n')

        inspection_data.save()

    else:
        message = f"Project with id = {data['id']} does not exis"

    print('*' * 100)

    matrix_value = determine_matrix(probability_rating,
                                    overall_consequence_rating)
    # matrix_value = determine_matrix('High',
    #                                 'High')


    return JsonResponse({
        'message': 'Data Received',
        'economic_aspects_consequence_factor': economic_aspects_consequence_factor,
        'economic_aspects_consequence_rating': economic_aspects_consequence_rating,
        'health_and_safety_aspects_consequence_factor': health_and_safety_aspects_consequence_factor,
        'health_and_safety_aspects_consequence_rating': health_and_safety_aspects_consequence_rating,
        'environmental_aspects_consequence_factor': environmental_aspects_consequence_factor,
        'environmental_aspects_consequence_rating': environmental_aspects_consequence_rating,
        'probability_factor': probability_factor,
        'probability_rating': probability_rating,
        'overall_consequence_factor': overall_consequence_factor,
        'overall_consequence_rating': overall_consequence_rating,
        'matrix_value': matrix_value,
        'corrosion_rate': corrosion_rate,
        'acceleration_factor_for_pitting_score': acceleration_factor_for_pitting_score,
        'adjusted_corrosion_rate': adjusted_corrosion_rate,
        'remaining_life': remaining_life,
        'k_initial': k_initial,
        'k_conf': k_conf,
        'k_final': k_final,
        'interval_between_next_required_inspection': interval_between_next_required_inspection
    })


@require_POST
@csrf_exempt
def update_project(request):
    data = json.loads(request.body)
    project = Project.objects.filter(id=data['id'])
    if project.exists():
        obj = project.first()
        obj.name = data['name']
        obj.description = data['description']
        obj.start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
        obj.end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
        obj.save()
    return JsonResponse({
        'message': 'Project was updated successfully'
    })


def get_user(request):
    user = None
    # if request.user.is_authenticated:
        # user = request.user.username
    # else:
        # user = 'Anonymous'
    user = User.objects.filter(is_superuser=True)
    user = user.first().username
    return JsonResponse({
        'user': user
    })


@require_POST
@csrf_exempt
def delete_project(request):
    data = json.loads(request.body)
    project = Project.objects.filter(pk=data['id'])
    message = None
    if project.exists():
        obj = project.first()
        obj.delete()
        message = "Project was deleted successfully"
    else:
        message = "Project was not delete"
    return JsonResponse({
        'message': message
    })
