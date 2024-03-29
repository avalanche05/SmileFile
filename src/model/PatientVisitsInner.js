/**
 * SmileFile
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PatientVisitsInner model module.
 * @module model/PatientVisitsInner
 * @version 1.0.0
 */
class PatientVisitsInner {
    /**
     * Constructs a new <code>PatientVisitsInner</code>.
     * @alias module:model/PatientVisitsInner
     */
    constructor() { 
        
        PatientVisitsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PatientVisitsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientVisitsInner} obj Optional instance to populate.
     * @return {module:model/PatientVisitsInner} The populated <code>PatientVisitsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientVisitsInner();

            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'Date');
            }
            if (data.hasOwnProperty('diagnosis')) {
                obj['diagnosis'] = ApiClient.convertToType(data['diagnosis'], 'String');
            }
            if (data.hasOwnProperty('treatment')) {
                obj['treatment'] = ApiClient.convertToType(data['treatment'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientVisitsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientVisitsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['diagnosis'] && !(typeof data['diagnosis'] === 'string' || data['diagnosis'] instanceof String)) {
            throw new Error("Expected the field `diagnosis` to be a primitive type in the JSON string but got " + data['diagnosis']);
        }
        // ensure the json data is a string
        if (data['treatment'] && !(typeof data['treatment'] === 'string' || data['treatment'] instanceof String)) {
            throw new Error("Expected the field `treatment` to be a primitive type in the JSON string but got " + data['treatment']);
        }

        return true;
    }


}



/**
 * Дата посещения
 * @member {Date} date
 */
PatientVisitsInner.prototype['date'] = undefined;

/**
 * Диагноз
 * @member {String} diagnosis
 */
PatientVisitsInner.prototype['diagnosis'] = undefined;

/**
 * Лечение
 * @member {String} treatment
 */
PatientVisitsInner.prototype['treatment'] = undefined;






export default PatientVisitsInner;

