# Changelog

## [Unreleased](https://github.com/mintproject/model-catalog-api/tree/HEAD)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.4.0...HEAD)

**Fixed bugs:**

- Fix unit tests v1.5.0 [\#120](https://github.com/mintproject/model-catalog-api/issues/120)
- 400 on GET softwareImages [\#119](https://github.com/mintproject/model-catalog-api/issues/119)
- Login not working in npm client 2.5.0-dev.0 [\#118](https://github.com/mintproject/model-catalog-api/issues/118)
- Position not being initialized in setups leads to indefinitely waiting to be run [\#115](https://github.com/mintproject/model-catalog-api/issues/115)

**Closed issues:**

- The API is not returning some properties  [\#116](https://github.com/mintproject/model-catalog-api/issues/116)
- Get output variables and region name on get customModelconfigurationsetupsVariableGet [\#113](https://github.com/mintproject/model-catalog-api/issues/113)
- /custom/modelconfigurationsetups/{id} does not return hasPresentation, hasStandarVariable [\#110](https://github.com/mintproject/model-catalog-api/issues/110)
- Get Model by Id returns no data on hasFunding [\#107](https://github.com/mintproject/model-catalog-api/issues/107)
- Insert subresource without id [\#103](https://github.com/mintproject/model-catalog-api/issues/103)
- Get Setup by Variable name [\#89](https://github.com/mintproject/model-catalog-api/issues/89)
- custom queries is not returning the type of sub resources [\#85](https://github.com/mintproject/model-catalog-api/issues/85)

**Merged pull requests:**

- fix: custom query [\#130](https://github.com/mintproject/model-catalog-api/pull/130) ([mosoriob](https://github.com/mosoriob))
- add dt query [\#129](https://github.com/mintproject/model-catalog-api/pull/129) ([mosoriob](https://github.com/mosoriob))
- use obasparql 3.4.1 [\#128](https://github.com/mintproject/model-catalog-api/pull/128) ([mosoriob](https://github.com/mosoriob))
- use oba 3.4.0 [\#127](https://github.com/mintproject/model-catalog-api/pull/127) ([mosoriob](https://github.com/mosoriob))
- sd 1.7.0 and sdm 1.6.0 [\#126](https://github.com/mintproject/model-catalog-api/pull/126) ([mosoriob](https://github.com/mosoriob))
- Fix tests [\#121](https://github.com/mintproject/model-catalog-api/pull/121) ([mosoriob](https://github.com/mosoriob))
- fix: tests [\#117](https://github.com/mintproject/model-catalog-api/pull/117) ([mosoriob](https://github.com/mosoriob))
- F\#88 [\#109](https://github.com/mintproject/model-catalog-api/pull/109) ([mosoriob](https://github.com/mosoriob))
- fix: allow multiple user [\#108](https://github.com/mintproject/model-catalog-api/pull/108) ([mosoriob](https://github.com/mosoriob))
- F\#84 [\#106](https://github.com/mintproject/model-catalog-api/pull/106) ([maurya-rohit](https://github.com/maurya-rohit))
- Fixing openapi [\#80](https://github.com/mintproject/model-catalog-api/pull/80) ([mosoriob](https://github.com/mosoriob))

## [1.4.0](https://github.com/mintproject/model-catalog-api/tree/1.4.0) (2020-03-17)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.4.0-dev0.0...1.4.0)

**Closed issues:**

- \[bug\] Texas is partOf travis and travis is partOf texas [\#104](https://github.com/mintproject/model-catalog-api/issues/104)
- POST Setup is creating resources even when ID is provided. [\#102](https://github.com/mintproject/model-catalog-api/issues/102)
- Regions are not returning partOf [\#100](https://github.com/mintproject/model-catalog-api/issues/100)
- get unitest for all classes [\#99](https://github.com/mintproject/model-catalog-api/issues/99)
- Setups are returning no data on adjustableParameter [\#98](https://github.com/mintproject/model-catalog-api/issues/98)
- Use ReDoc [\#97](https://github.com/mintproject/model-catalog-api/issues/97)
- Framing is failing when two properties with the same range points to the same resource [\#96](https://github.com/mintproject/model-catalog-api/issues/96)
- Insert nested resources [\#69](https://github.com/mintproject/model-catalog-api/issues/69)

**Merged pull requests:**

- Fixing recursive insert bug [\#101](https://github.com/mintproject/model-catalog-api/pull/101) ([mosoriob](https://github.com/mosoriob))

## [1.4.0-dev0.0](https://github.com/mintproject/model-catalog-api/tree/1.4.0-dev0.0) (2020-03-11)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.4.0-dev0...1.4.0-dev0.0)

## [1.4.0-dev0](https://github.com/mintproject/model-catalog-api/tree/1.4.0-dev0) (2020-03-10)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.3.2-0...1.4.0-dev0)

**Closed issues:**

- Get Parameter "relevant for intervention" [\#90](https://github.com/mintproject/model-catalog-api/issues/90)
- swagger ui takes a lot time to load [\#86](https://github.com/mintproject/model-catalog-api/issues/86)
-  searching by variable [\#78](https://github.com/mintproject/model-catalog-api/issues/78)

**Merged pull requests:**

- Feature\#travis [\#93](https://github.com/mintproject/model-catalog-api/pull/93) ([mosoriob](https://github.com/mosoriob))
- Fixed recursive insert bug [\#91](https://github.com/mintproject/model-catalog-api/pull/91) ([mosoriob](https://github.com/mosoriob))

## [1.3.2-0](https://github.com/mintproject/model-catalog-api/tree/1.3.2-0) (2020-02-28)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.3.1...1.3.2-0)

**Closed issues:**

- Get Model by Variable name [\#88](https://github.com/mintproject/model-catalog-api/issues/88)

## [1.3.1](https://github.com/mintproject/model-catalog-api/tree/1.3.1) (2020-02-27)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.3.0...1.3.1)

**Fixed bugs:**

- \[Client\] Problems with setup parameter assign method [\#60](https://github.com/mintproject/model-catalog-api/issues/60)

**Closed issues:**

- Crash in app.add\_api\(\) and extreme startup slowness [\#82](https://github.com/mintproject/model-catalog-api/issues/82)
- POST: Inserting inner resources is not working [\#81](https://github.com/mintproject/model-catalog-api/issues/81)
- Missing relationships between Regions [\#79](https://github.com/mintproject/model-catalog-api/issues/79)
- Release model catalog fetch package [\#77](https://github.com/mintproject/model-catalog-api/issues/77)
- search by label, category, label [\#76](https://github.com/mintproject/model-catalog-api/issues/76)
- Create a list of the classes to show on the model catalog api [\#75](https://github.com/mintproject/model-catalog-api/issues/75)
- Prepare materials \(Notebooks\) 2 [\#74](https://github.com/mintproject/model-catalog-api/issues/74)
- Prepare materials \(Notebooks\) 3 [\#73](https://github.com/mintproject/model-catalog-api/issues/73)
- Prepare materials \(Notebooks\) for: [\#72](https://github.com/mintproject/model-catalog-api/issues/72)
- Support variable, region search [\#70](https://github.com/mintproject/model-catalog-api/issues/70)
- Error on PUT ModelConfiguration [\#66](https://github.com/mintproject/model-catalog-api/issues/66)
- GET TimeInvervals does not return all the data [\#40](https://github.com/mintproject/model-catalog-api/issues/40)
- Example on how to use PUT [\#19](https://github.com/mintproject/model-catalog-api/issues/19)

**Merged pull requests:**

- Add custom queries [\#71](https://github.com/mintproject/model-catalog-api/pull/71) ([mosoriob](https://github.com/mosoriob))
- add path custom model configuration [\#67](https://github.com/mintproject/model-catalog-api/pull/67) ([mosoriob](https://github.com/mosoriob))
- enable custom queries [\#65](https://github.com/mintproject/model-catalog-api/pull/65) ([mosoriob](https://github.com/mosoriob))

## [1.3.0](https://github.com/mintproject/model-catalog-api/tree/1.3.0) (2019-12-18)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.2.6...1.3.0)

## [1.2.6](https://github.com/mintproject/model-catalog-api/tree/1.2.6) (2019-12-13)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.2.5...1.2.6)

**Closed issues:**

- sd:hasMaximumAcceptedValue must be a string, integer o float [\#64](https://github.com/mintproject/model-catalog-api/issues/64)

## [1.2.5](https://github.com/mintproject/model-catalog-api/tree/1.2.5) (2019-12-06)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.2.4...1.2.5)

**Closed issues:**

- POST SampleResource writes on prov:value and not in sd:value [\#62](https://github.com/mintproject/model-catalog-api/issues/62)

**Merged pull requests:**

- fix: uri for sd:value [\#63](https://github.com/mintproject/model-catalog-api/pull/63) ([mosoriob](https://github.com/mosoriob))

## [1.2.4](https://github.com/mintproject/model-catalog-api/tree/1.2.4) (2019-11-21)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.2.3...1.2.4)

**Fixed bugs:**

- If an ID has spaces, the API returns an error [\#23](https://github.com/mintproject/model-catalog-api/issues/23)

**Closed issues:**

- \[Client\] Problem creating parameters with fixedValue [\#61](https://github.com/mintproject/model-catalog-api/issues/61)
- POST on modelConfiguration [\#53](https://github.com/mintproject/model-catalog-api/issues/53)
- GET modelConfiguration does not return hasComponentLocation for most models [\#49](https://github.com/mintproject/model-catalog-api/issues/49)
- API should be created from the ontology [\#22](https://github.com/mintproject/model-catalog-api/issues/22)
- Use URIs as ids [\#21](https://github.com/mintproject/model-catalog-api/issues/21)

## [1.2.3](https://github.com/mintproject/model-catalog-api/tree/1.2.3) (2019-11-21)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.2.2...1.2.3)

## [1.2.2](https://github.com/mintproject/model-catalog-api/tree/1.2.2) (2019-11-20)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.2.1...1.2.2)

**Closed issues:**

- \[Client\] SampleResource does not return value [\#59](https://github.com/mintproject/model-catalog-api/issues/59)

## [1.2.1](https://github.com/mintproject/model-catalog-api/tree/1.2.1) (2019-11-12)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.2.1-dev...1.2.1)

## [1.2.1-dev](https://github.com/mintproject/model-catalog-api/tree/1.2.1-dev) (2019-11-12)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.2.0-dev...1.2.1-dev)

**Closed issues:**

- Region API does not return all the regions [\#57](https://github.com/mintproject/model-catalog-api/issues/57)

## [1.2.0-dev](https://github.com/mintproject/model-catalog-api/tree/1.2.0-dev) (2019-11-01)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.8...1.2.0-dev)

**Closed issues:**

- DELETE on modelConfiguration [\#52](https://github.com/mintproject/model-catalog-api/issues/52)
- GET SoftwareImage/WEATHER-GENERATOR:LATEST does not work [\#43](https://github.com/mintproject/model-catalog-api/issues/43)

**Merged pull requests:**

- Release v1.2.0 [\#58](https://github.com/mintproject/model-catalog-api/pull/58) ([mosoriob](https://github.com/mosoriob))

## [1.1.8](https://github.com/mintproject/model-catalog-api/tree/1.1.8) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.8-0...1.1.8)

## [1.1.8-0](https://github.com/mintproject/model-catalog-api/tree/1.1.8-0) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.8-1...1.1.8-0)

## [1.1.8-1](https://github.com/mintproject/model-catalog-api/tree/1.1.8-1) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.7...1.1.8-1)

## [1.1.7](https://github.com/mintproject/model-catalog-api/tree/1.1.7) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.7-5...1.1.7)

## [1.1.7-5](https://github.com/mintproject/model-catalog-api/tree/1.1.7-5) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.7-4...1.1.7-5)

## [1.1.7-4](https://github.com/mintproject/model-catalog-api/tree/1.1.7-4) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.7-3...1.1.7-4)

## [1.1.7-3](https://github.com/mintproject/model-catalog-api/tree/1.1.7-3) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.7-2...1.1.7-3)

## [1.1.7-2](https://github.com/mintproject/model-catalog-api/tree/1.1.7-2) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.7-1...1.1.7-2)

## [1.1.7-1](https://github.com/mintproject/model-catalog-api/tree/1.1.7-1) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.7-0...1.1.7-1)

## [1.1.7-0](https://github.com/mintproject/model-catalog-api/tree/1.1.7-0) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.6...1.1.7-0)

## [1.1.6](https://github.com/mintproject/model-catalog-api/tree/1.1.6) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.5...1.1.6)

**Merged pull requests:**

- Super auto deploy [\#54](https://github.com/mintproject/model-catalog-api/pull/54) ([mosoriob](https://github.com/mosoriob))

## [1.1.5](https://github.com/mintproject/model-catalog-api/tree/1.1.5) (2019-10-19)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.5-dev...1.1.5)

**Closed issues:**

- POST Parameters does not work [\#51](https://github.com/mintproject/model-catalog-api/issues/51)
- Query to get all model configuration of some region [\#50](https://github.com/mintproject/model-catalog-api/issues/50)
- GET modelConfigurations does not return hasCalibration / hasSetup [\#48](https://github.com/mintproject/model-catalog-api/issues/48)
- \[Client\] GET modelConfiguration does not always return Keywords, Author and SoftwareDescription [\#47](https://github.com/mintproject/model-catalog-api/issues/47)
- Return value for POST and PUT [\#46](https://github.com/mintproject/model-catalog-api/issues/46)
- Error on PUT modelConfiguration [\#39](https://github.com/mintproject/model-catalog-api/issues/39)
- Release v0.0.3 [\#26](https://github.com/mintproject/model-catalog-api/issues/26)

## [1.1.5-dev](https://github.com/mintproject/model-catalog-api/tree/1.1.5-dev) (2019-10-11)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.4-dev...1.1.5-dev)

## [1.1.4-dev](https://github.com/mintproject/model-catalog-api/tree/1.1.4-dev) (2019-10-10)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.3-dev...1.1.4-dev)

**Closed issues:**

- GET Grid does not return Spatial resolution, Dimensions and Shape [\#44](https://github.com/mintproject/model-catalog-api/issues/44)
- Parameters and DatasetSpecifications does not return sd:position [\#42](https://github.com/mintproject/model-catalog-api/issues/42)
- Get models does not return description, keywords, component location etc. [\#41](https://github.com/mintproject/model-catalog-api/issues/41)
- CORS when trying to PUT [\#38](https://github.com/mintproject/model-catalog-api/issues/38)
- sd:DatasetSpecification should return sd:description [\#34](https://github.com/mintproject/model-catalog-api/issues/34)

**Merged pull requests:**

- Context [\#45](https://github.com/mintproject/model-catalog-api/pull/45) ([mosoriob](https://github.com/mosoriob))

## [1.1.3-dev](https://github.com/mintproject/model-catalog-api/tree/1.1.3-dev) (2019-10-10)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.2-dev...1.1.3-dev)

**Closed issues:**

- sd:Parameter must return sd:usesUnit [\#32](https://github.com/mintproject/model-catalog-api/issues/32)

## [1.1.2-dev](https://github.com/mintproject/model-catalog-api/tree/1.1.2-dev) (2019-10-09)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.1-dev...1.1.2-dev)

## [1.1.1-dev](https://github.com/mintproject/model-catalog-api/tree/1.1.1-dev) (2019-10-09)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.1.0-dev...1.1.1-dev)

## [1.1.0-dev](https://github.com/mintproject/model-catalog-api/tree/1.1.0-dev) (2019-10-09)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.0.0...1.1.0-dev)

## [1.0.0](https://github.com/mintproject/model-catalog-api/tree/1.0.0) (2019-10-08)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/1.0.0-dev...1.0.0)

**Closed issues:**

- Search for label [\#35](https://github.com/mintproject/model-catalog-api/issues/35)
- rdfs label must be a array [\#31](https://github.com/mintproject/model-catalog-api/issues/31)
- Log out is not implemented [\#18](https://github.com/mintproject/model-catalog-api/issues/18)

**Merged pull requests:**

- Develop [\#37](https://github.com/mintproject/model-catalog-api/pull/37) ([mosoriob](https://github.com/mosoriob))
- Search [\#36](https://github.com/mintproject/model-catalog-api/pull/36) ([mosoriob](https://github.com/mosoriob))
- Release [\#33](https://github.com/mintproject/model-catalog-api/pull/33) ([mosoriob](https://github.com/mosoriob))

## [1.0.0-dev](https://github.com/mintproject/model-catalog-api/tree/1.0.0-dev) (2019-10-07)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/v0.0.2...1.0.0-dev)

**Merged pull requests:**

- Dev [\#30](https://github.com/mintproject/model-catalog-api/pull/30) ([mosoriob](https://github.com/mosoriob))
- Req [\#28](https://github.com/mintproject/model-catalog-api/pull/28) ([mosoriob](https://github.com/mosoriob))
- Add: first release v1.0.0  [\#27](https://github.com/mintproject/model-catalog-api/pull/27) ([mosoriob](https://github.com/mosoriob))
- Add: mysql support [\#24](https://github.com/mintproject/model-catalog-api/pull/24) ([mosoriob](https://github.com/mosoriob))

## [v0.0.2](https://github.com/mintproject/model-catalog-api/tree/v0.0.2) (2019-06-09)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/v0.1...v0.0.2)

**Closed issues:**

- Consolidate GRLC and Swagger APIs [\#12](https://github.com/mintproject/model-catalog-api/issues/12)
- json\_convert must use embedding  [\#10](https://github.com/mintproject/model-catalog-api/issues/10)

## [v0.1](https://github.com/mintproject/model-catalog-api/tree/v0.1) (2019-04-16)

[Full Changelog](https://github.com/mintproject/model-catalog-api/compare/7e6bb47d2450b647b23f192573ad44a7e4661daa...v0.1)

**Closed issues:**

- Modify JSON response to align with the request and ontology  [\#9](https://github.com/mintproject/model-catalog-api/issues/9)
- Align JSON format with MINT ontology [\#8](https://github.com/mintproject/model-catalog-api/issues/8)
- Rename dataset to dataset specification [\#7](https://github.com/mintproject/model-catalog-api/issues/7)
- Deploy [\#5](https://github.com/mintproject/model-catalog-api/issues/5)
- Insert triples in user graph [\#4](https://github.com/mintproject/model-catalog-api/issues/4)
- Rewrite the examples from JSON to JSON-LD [\#2](https://github.com/mintproject/model-catalog-api/issues/2)
- User and support jwt auth [\#1](https://github.com/mintproject/model-catalog-api/issues/1)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
