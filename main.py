"""
* * Covid Interface * *
*
* Application used to interact with the Covid Act Now API
* An API key is required to use the API
* Author: Josh Ryther
"""


import configparser
import requests
import json

class CovidInterface:
    def __init__(self):
        """
        * An API key must be listed in an ini file at the root of the project
        * The section must be labeled as 'API'
        * The property must be labeled as 'Key'
        """
        self.config = configparser.ConfigParser() # Initilize ini file parser
        self.config.read('APIFile.ini')
        self.key = self.config['API']['Key'] # Assign API key to variable

    """
    * * Create a URL for Covid Now Endpoints * *
    * 
    * - type must be either 'json' or 'csv'
    * - location must be 'country', 'state', 'county', or 'cbsa'
    * - sublocation (Leave blank if further filtering is not required):
    *   - country: 'US"
    *   - state: Two letter state code (example 'AK' for alaska)
    *   - county: 5 digit FIPS code
    *   - cbsa: cbsa code for metropolitan areas
    * - timeseries is 'historic' if historical data is needed.  Otherwise leave blank.
    """
    def urlBuilder(self, type, location, sublocation = '', timeseries = ''):
        url = 'https://api.covidactnow.org/v2/'
        if sublocation == '':
            if location == 'country':
                url += ('country/US')
            elif location == 'state':
                url += ('states')
            elif location == 'county':
                url += ('counties')
            elif location == 'state':
                url += ('cbsas')
        elif sublocation != '':
            if location == 'country':
                url += ('country/US')
            elif location == 'state':
                url += ('state/' + sublocation)
            elif location == 'county':
                url += ('county/' + sublocation)
            elif location == 'state':
                url += ('cbsa/' + sublocation)
        if timeseries == 'historic':
            url += '.timeseries'
        url += ('.' + type)
        url += ('?apiKey=' + self.key)
        return url

    """
    * * Make a request to the Covid Now API * *
    *
    * A url is passed as an argument and a request is made using it.
    * The function returns the body of the request as JSON
    """
    def makeRequest(self, url):
        request = requests.get(url) # Make request to API
        response = request.text # Retrieve body of request
        data = json.loads(response) # Convert to JSON
        return data

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