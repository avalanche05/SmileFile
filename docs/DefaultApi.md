# SmileFile.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patientsGet**](DefaultApi.md#patientsGet) | **GET** /patients | Получить список всех пациентов
[**patientsPatientIdGet**](DefaultApi.md#patientsPatientIdGet) | **GET** /patients/{patientId} | Получить конкретного пациента
[**patientsPatientIdPut**](DefaultApi.md#patientsPatientIdPut) | **PUT** /patients/{patientId} | Обновить информацию о пациенте
[**patientsPost**](DefaultApi.md#patientsPost) | **POST** /patients | Добавить нового пациента



## patientsGet

> [Patient] patientsGet()

Получить список всех пациентов

### Example

```javascript
import SmileFile from 'smile_file';

let apiInstance = new SmileFile.DefaultApi();
apiInstance.patientsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Patient]**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patientsPatientIdGet

> Patient patientsPatientIdGet(patientId)

Получить конкретного пациента

### Example

```javascript
import SmileFile from 'smile_file';

let apiInstance = new SmileFile.DefaultApi();
let patientId = "patientId_example"; // String | 
apiInstance.patientsPatientIdGet(patientId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patientId** | **String**|  | 

### Return type

[**Patient**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patientsPatientIdPut

> Patient patientsPatientIdPut(patientId, patient)

Обновить информацию о пациенте

### Example

```javascript
import SmileFile from 'smile_file';

let apiInstance = new SmileFile.DefaultApi();
let patientId = "patientId_example"; // String | 
let patient = new SmileFile.Patient(); // Patient | 
apiInstance.patientsPatientIdPut(patientId, patient, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patientId** | **String**|  | 
 **patient** | [**Patient**](Patient.md)|  | 

### Return type

[**Patient**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patientsPost

> Patient patientsPost(patient)

Добавить нового пациента

### Example

```javascript
import SmileFile from 'smile_file';

let apiInstance = new SmileFile.DefaultApi();
let patient = new SmileFile.Patient(); // Patient | 
apiInstance.patientsPost(patient, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patient** | [**Patient**](Patient.md)|  | 

### Return type

[**Patient**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

