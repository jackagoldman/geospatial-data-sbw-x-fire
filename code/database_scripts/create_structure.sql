-- Script to create tables/ database structure for the paired_defol_nondefol database
-- Author: Jack A. Goldman
-- Date: 01/11/2024

-- create key
CREATE TABLE fire_key(
    id integer PRIMARY KEY,
    fire_name character varying,
    year bigint,
    defol boolean, -- Use 1 or 0 to specify whether it is the defolaited or non defoliated perimeter... use as a key?
)

-- create insect_disturbance table
CREATE DATABASE insect_disturbance(
    id integer PRIMARY KEY,
    fire_name character varying,
    tsd integer,
    years_defoliated integer
)

-- create nbr recovery table for defoliated fires 
CREATE TABLE defol_nbr_recovery(
    id integer PRIMARY KEY,
    fire_name character varying, 
    defol_nbr_1 bigint,
    defol_nbr_2 bigint,
    defol_nbr_3 bigint,
    defol_nbr_4 bigint,
    defol_nbr_5 bigint, 
    defol_nbr_6 bigint, 
    defol_nbr_7 bigint, 
    defol_nbr_8 bigint, 
    defol_nbr_9 bigint, 
    defol_nbr_10 bigint
)

-- create nbr recovery table for non-defoliated fires 
CREATE TABLE nondefol_nbr_recovery(
    id integer PRIMARY KEY,
    fire_name character varying, 
    nondefol_nbr_1 bigint,
    nondefol_nbr_2 bigint,
    nondefol_nbr_3 bigint,
    nondefol_nbr_4 bigint,
    nondefol_nbr_5 bigint, 
    nondefol_nbr_6 bigint, 
    nondefol_nbr_7 bigint, 
    nondefol_nbr_8 bigint, 
    nondefol_nbr_9 bigint, 
    nondefol_nbr_10 bigint
)
-- create burn severity table for defol fires 
CREATE TABLE defol_burn_severity(
    id integer PRIMARY KEY,
    fire_name character varying,
    defol_rbr_median bigint,
    defol_rbr_extreme bigint,
    defol_rbr_cv bigint
)

-- create burn severity table for nondefol fires 
CREATE TABLE nondefol_burn_severity(
    id integer PRIMARY KEY,
    fire_name character varying,
    nondefol_rbr_median bigint,
    nondefol_rbr_extreme bigint,
    nondefol_rbr_cv bigint
)

-- forest cover for defoliated fires
CREATE TABLE defol_forest_cover(
    id integer PRIMARY KEY,
    fire_name character varying,
    defol_biomass bigint,
    defol_stand_age bigint,
    defol_canopy_closure bigint
)

-- forest cover for nondefoliated fires
CREATE TABLE defol_forest_cover(
    id integer PRIMARY KEY,
    fire_name character varying,
    nondefol_biomass bigint,
    nondefol_stand_age bigint,
    nondefol_canopy_closure bigint
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

-- create table for defoliated fire characteristics
CREATE TABLE defol_fire_characteristics(
    id integer PRIMARY KEY,
    fire_name character varying,
    defol_perimeter bigint,
    defol_area bigint,
    defol_shapeindex bigint,
    defol_burnday integer,
)

-- create table for nondefoliated fire characteristics
CREATE TABLE nondefol_fire_characteristics(
    id integer PRIMARY KEY,
    fire_name character varying,
    nondefol_perimeter bigint,
    nondefol_area bigint,
    nondefol_shapeindex bigint,
    nondefol_burnday integer,
)

-- create snow cover table for defoliated fires
CREATE TABLE snow_cover(
    id integer PRIMARY KEY,
    fire_name character varying,
    defol_sfd integer,
    defol_sf
)

-- create spatial data table for defoliated
CREATE TABLE defol_spatial(
    id ineger PRIMARY KEY,
    fire_name character varying,
    defol_fire_geometry polygon,
    defol_fire_centroid point
)