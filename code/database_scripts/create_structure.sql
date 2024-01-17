-- Script to create tables/ database structure for the paired_defol_nondefol database
-- Author: Jack A. Goldman
-- Date: 01/11/2024

-- create key
CREATE TABLE fire_key(
    id integer PRIMARY KEY,
    fire_name character varying,
    year bigint,
)

-- create insect_disturbance table
CREATE DATABASE insect_disturbance(
    id integer PRIMARY KEY,
    fire_name character varying,
    tsd integer,
    years_defoliated integer,
    defol boolean, -- Use 1 or 0 to specify whether it is the defolaited or non defoliated perimeter... use as a key?

)

-- create nbr recovery table for defoliated fires 
CREATE TABLE nbr_recovery(
    id integer PRIMARY KEY,
    fire_name character varying, 
    nbr_1 bigint,
    nbr_2 bigint,
    nbr_3 bigint,
    nbr_4 bigint,
    nbr_5 bigint, 
    nbr_6 bigint, 
    nbr_7 bigint, 
    nbr_8 bigint, 
    nbr_9 bigint, 
    nbr_10 bigint
)

-- create burn severity table for defol fires 
CREATE TABLE burn_severity(
    id integer PRIMARY KEY,
    fire_name character varying,
    rbr_median bigint,
    rbr_extreme bigint,
    rbr_cv bigint
)

-- forest cover 
CREATE TABLE forest_cover(
    id integer PRIMARY KEY,
    fire_name character varying,
    biomass bigint,
    stand_age bigint,
    canopy_closure bigint
)

-- create weather data (fwi-90th-fire-duration.csv)
CREATE TABLE fwi_duration(
    id integer PRIMARY KEY, 
    fire_name character varying,
    isi_duration bigint, 
    bui_duration bigint, 
    fwi_duration bigint,
    dc_duration bigint,
    ffmc_duration bigint,
    dmc_duration bigint
)

-- create table for  fire characteristics
CREATE TABLE fire_characteristics(
    id integer PRIMARY KEY,
    fire_name character varying,
    burn_day integer
)

-- create snow cover table for defoliated fires
CREATE TABLE snow_cover(
    id integer PRIMARY KEY,
    fire_name character varying,
    sfd integer,
    swe integer
)

-- create spatial information tablr
CREATE TABLE defol_spatial_information(
    id ineger PRIMARY KEY,
    fire_geometry polygon,
    fire_centroid point,
    fire_perimeter_m bigint,
    fire_area_ha bigint,
    fire_area_m bigint,
    fire_shape_index bigint,
)

-- create harvesting table

CREATE TABLE harvest(




    
)