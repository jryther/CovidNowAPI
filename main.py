import configparser
import requests
import json
import pandas as pd

config = configparser.ConfigParser()
config.read('APIFile.ini')
key = config['API']['ApiKey']
endpoint = config['API']['endpoint']

url = endpoint + 'states.json?apiKey=' + key

request = requests.get(url)
response = request.text
data = json.loads(response)
df = pd.DataFrame.from_records(data)


"""
JSON document example passed by the API

{
  "fips": "string",
  "country": "string",
  "state": "string",
  "county": "string",
  "level": "country",
  "lat": 0,
  "locationId": "string",
  "long": 0,
  "population": 0,
  "metrics": {
    "testPositivityRatio": 0,
    "testPositivityRatioDetails": {
      "source": "CMSTesting"
    },
    "caseDensity": 0,
    "contactTracerCapacityRatio": 0,
    "infectionRate": 0,
    "infectionRateCI90": 0,
    "icuHeadroomRatio": 0,
    "icuHeadroomDetails": {
      "currentIcuCovid": 0,
      "currentIcuCovidMethod": "actual",
      "currentIcuNonCovid": 0,
      "currentIcuNonCovidMethod": "actual"
    },
    "icuCapacityRatio": 0,
    "vaccinationsInitiatedRatio": 0,
    "vaccinationsCompletedRatio": 0
  },
  "riskLevels": {
    "overall": 0,
    "testPositivityRatio": 0,
    "caseDensity": 0,
    "contactTracerCapacityRatio": 0,
    "infectionRate": 0,
    "icuHeadroomRatio": 0,
    "icuCapacityRatio": 0
  },
  "cdcTransmissionLevel": 0,
  "actuals": {
    "cases": 0,
    "deaths": 0,
    "positiveTests": 0,
    "negativeTests": 0,
    "contactTracers": 0,
    "hospitalBeds": {
      "capacity": 0,
      "currentUsageTotal": 0,
      "currentUsageCovid": 0,
      "typicalUsageRate": 0
    },
    "icuBeds": {
      "capacity": 0,
      "currentUsageTotal": 0,
      "currentUsageCovid": 0,
      "typicalUsageRate": 0
    },
    "newCases": 0,
    "newDeaths": 0,
    "vaccinesDistributed": 0,
    "vaccinationsInitiated": 0,
    "vaccinationsCompleted": 0,
    "vaccinesAdministered": 0,
    "vaccinesAdministeredDemographics": {
      "age": {},
      "race": {},
      "ethnicity": {},
      "sex": {}
    },
    "vaccinationsInitiatedDemographics": {
      "age": {},
      "race": {},
      "ethnicity": {},
      "sex": {}
    }
  },
  "annotations": {
    "cases": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "deaths": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "positiveTests": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "negativeTests": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "contactTracers": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "hospitalBeds": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "icuBeds": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "newCases": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "newDeaths": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "vaccinesDistributed": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "vaccinationsInitiated": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "vaccinationsCompleted": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "vaccinesAdministered": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "testPositivityRatio": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "caseDensity": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "contactTracerCapacityRatio": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "infectionRate": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "infectionRateCI90": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "icuHeadroomRatio": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "icuCapacityRatio": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "vaccinationsInitiatedRatio": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    },
    "vaccinationsCompletedRatio": {
      "sources": [
        {
          "type": "NYTimes",
          "url": "string",
          "name": "string"
        }
      ],
      "anomalies": [
        {
          "date": "2019-08-24",
          "type": "cumulative_tail_truncated",
          "original_observation": 0
        }
      ]
    }
  },
  "lastUpdatedDate": "2019-08-24",
  "url": "string"
}
"""