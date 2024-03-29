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
import PatientVisitsInner from './PatientVisitsInner';

/**
 * The Patient model module.
 * @module model/Patient
 * @version 1.0.0
 */
class Patient {
    /**
     * Constructs a new <code>Patient</code>.
     * @alias module:model/Patient
     */
    constructor() { 
        
        Patient.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Patient</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Patient} obj Optional instance to populate.
     * @return {module:model/Patient} The populated <code>Patient</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Patient();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('contactDetails')) {
                obj['contactDetails'] = ApiClient.convertToType(data['contactDetails'], 'String');
            }
            if (data.hasOwnProperty('lastAppointment')) {
                obj['lastAppointment'] = ApiClient.convertToType(data['lastAppointment'], 'Date');
            }
            if (data.hasOwnProperty('visits')) {
                obj['visits'] = ApiClient.convertToType(data['visits'], [PatientVisitsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Patient</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Patient</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['contactDetails'] && !(typeof data['contactDetails'] === 'string' || data['contactDetails'] instanceof String)) {
            throw new Error("Expected the field `contactDetails` to be a primitive type in the JSON string but got " + data['contactDetails']);
        }
        if (data['visits']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['visits'])) {
                throw new Error("Expected the field `visits` to be an array in the JSON data but got " + data['visits']);
            }
            // validate the optional field `visits` (array)
            for (const item of data['visits']) {
                PatientVisitsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {String} id
 */
Patient.prototype['id'] = undefined;

/**
 * @member {String} name
 */
Patient.prototype['name'] = undefined;

/**
 * Контактные данные
 * @member {String} contactDetails
 */
Patient.prototype['contactDetails'] = undefined;

/**
 * Дата последнего посещения
 * @member {Date} lastAppointment
 */
Patient.prototype['lastAppointment'] = undefined;

/**
 * @member {Array.<module:model/PatientVisitsInner>} visits
 */
Patient.prototype['visits'] = undefined;






export default Patient;

