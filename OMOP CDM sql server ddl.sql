/*********************************************************************************
# Copyright 2018-08 Observational Health Data Sciences and Informatics
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
********************************************************************************/

/************************

 ####### #     # ####### ######      #####  ######  #     #            #####        ###
 #     # ##   ## #     # #     #    #     # #     # ##   ##    #    # #     #      #   #
 #     # # # # # #     # #     #    #       #     # # # # #    #    # #           #     #
 #     # #  #  # #     # ######     #       #     # #  #  #    #    # ######      #     #
 #     # #     # #     # #          #       #     # #     #    #    # #     # ### #     #
 #     # #     # #     # #          #     # #     # #     #     #  #  #     # ###  #   #
 ####### #     # ####### #           #####  ######  #     #      ##    #####  ###   ###

sql server script to create OMOP common data model version 6.0

last revised: 27-Aug-2018

Authors:  Patrick Ryan, Christian Reich, Clair Blacketer


*************************/



--HINT DISTRIBUTE ON RANDOM
CREATE TABLE concept (
  concept_id			    INTEGER			NOT NULL ,
  concept_name			  	VARCHAR(255)	NOT NULL ,
  domain_id				    VARCHAR(20)		NOT NULL ,
  vocabulary_id			  	VARCHAR(20)		NOT NULL ,
  concept_class_id			VARCHAR(20)		NOT NULL ,
  standard_concept			VARCHAR(1)		NULL ,
  concept_code			  	VARCHAR(50)		NOT NULL ,
  valid_start_date			DATE			NOT NULL ,
  valid_end_date		  	DATE			NOT NULL ,
  invalid_reason		  	VARCHAR(1)		NULL
)
;




--HINT DISTRIBUTE_ON_KEY(person_id)
CREATE TABLE person
(
  person_id						      BIGINT	  	NOT NULL , 
  gender_concept_id				      INTEGER	  	NOT NULL ,
  year_of_birth					      INTEGER	  	NOT NULL ,
  month_of_birth				      INTEGER	  	NULL,
  day_of_birth					      INTEGER	  	NULL,
  birth_datetime				      TIMESTAMP	  	NULL,
  race_concept_id				      INTEGER		NOT NULL,
  ethnicity_concept_id			  	  INTEGER	  	NOT NULL,
  location_id					      BIGINT		NULL,
  provider_id					      BIGINT		NULL,
  care_site_id					      BIGINT		NULL,
  person_source_value			      VARCHAR(50)   NULL,
  gender_source_value			      VARCHAR(50)   NULL,
  gender_source_concept_id	  		  INTEGER		NOT NULL,
  race_source_value				      VARCHAR(50)   NULL,
  race_source_concept_id		      INTEGER		NOT NULL,
  ethnicity_source_value		  	  VARCHAR(50)   NULL,
  ethnicity_source_concept_id		  INTEGER		NOT NULL
)
;


--HINT DISTRIBUTE_ON_KEY(person_id)
CREATE TABLE visit_occurrence
(
  visit_occurrence_id			BIGINT			NOT NULL ,
  person_id						BIGINT			NOT NULL ,
  visit_concept_id				INTEGER			NOT NULL ,
  visit_start_date				DATE			NULL ,
  visit_start_datetime			TIMESTAMP		NOT NULL ,
  visit_end_date				DATE			NULL ,
  visit_end_datetime			TIMESTAMP		NOT NULL ,
  visit_type_concept_id			INTEGER			NOT NULL ,
  provider_id					BIGINT			NULL,
  care_site_id					BIGINT			NULL,
  visit_source_value			VARCHAR(50)		NULL,
  visit_source_concept_id		INTEGER			NOT NULL ,
  admitted_from_concept_id      INTEGER     	NOT NULL ,   
  admitted_from_source_value    VARCHAR(50) 	NULL ,
  discharge_to_source_value		VARCHAR(50)		NULL ,
  discharge_to_concept_id		INTEGER   		NULL ,
  preceding_visit_occurrence_id	BIGINT			NULL
)
;


--HINT DISTRIBUTE_ON_KEY(person_id)
CREATE TABLE drug_exposure
(
  drug_exposure_id				BIGINT			NOT NULL ,
  person_id						BIGINT			NOT NULL ,
  drug_concept_id				INTEGER			NOT NULL ,
  drug_exposure_start_date		DATE			NULL ,
  drug_exposure_start_datetime	TIMESTAMP		NOT NULL ,
  drug_exposure_end_date		DATE			NULL ,
  drug_exposure_end_datetime	TIMESTAMP		NOT NULL ,
  verbatim_end_date				DATE			NULL ,
  drug_type_concept_id			INTEGER			NOT NULL ,
  stop_reason					VARCHAR(20)		NULL ,
  refills						INTEGER		  	NULL ,
  quantity						NUMERIC			NULL ,
  days_supply					INTEGER		  	NULL ,
  sig							TEXT	NULL ,
  route_concept_id				INTEGER			NOT NULL ,
  lot_number					VARCHAR(50)	  	NULL ,
  provider_id					BIGINT			NULL ,
  visit_occurrence_id			BIGINT			NULL ,
  visit_detail_id               BIGINT       	NULL ,
  drug_source_value				VARCHAR(50)	  	NULL ,
  drug_source_concept_id		INTEGER			NOT NULL ,
  route_source_value			VARCHAR(50)		NULL ,
  dose_unit_source_value		VARCHAR(50)	  	NULL
)
;

--HINT DISTRIBUTE_ON_KEY(person_id)
CREATE TABLE condition_occurrence
(
  condition_occurrence_id		BIGINT			NOT NULL ,
  person_id						BIGINT			NOT NULL ,
  condition_concept_id			INTEGER			NOT NULL ,
  condition_start_date			DATE			NULL ,
  condition_start_datetime		TIMESTAMP		NOT NULL ,
  condition_end_date			DATE			NULL ,
  condition_end_datetime		TIMESTAMP		NULL ,
  condition_type_concept_id		INTEGER			NOT NULL ,
  condition_status_concept_id	INTEGER			NULL ,
  stop_reason					VARCHAR(20)		NULL ,
  provider_id					BIGINT			NULL ,
  visit_occurrence_id			BIGINT			NULL ,
  visit_detail_id               BIGINT     		NULL ,
  condition_source_value		VARCHAR(50)		NULL ,
  condition_source_concept_id	INTEGER			NULL ,
  condition_status_source_value	VARCHAR(50)		NULL
)
;


--HINT DISTRIBUTE_ON_KEY(person_id)
CREATE TABLE death
(
	person_id							BIGINT			NOT NULL ,
	death_date		DATE		NOT NULL ,
	death_datetime		TIMESTAMP		 NULL ,
	death_type_concept_id  INTEGER       NOT NULL ,
	cause_concept_id 	INTEGER       NOT NULL ,
	cause_source_value VARCHAR(50)		NULL ,
	cause_source_concept_id INTEGER NOT NULL
)
;
