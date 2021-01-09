%module coast_wrapper
%{
#include <crs/CorsikaTypes.h>
#include <crs/TParticleBlockEntry.h>

#include <crsRead/MCorsikaReader.h>

#include <crs/TSubBlock.h>
#include <crs/MRunHeader.h>
#include <crs/MEventHeader.h>
#include <crs/MEventEnd.h>
#include <crs/MParticleBlock.h>
#include <crs/MLongitudinalBlock.h>
#include <crs/MParticle.h>

#include <custom_accessors.cpp>
%}

%include std_string.i
%include std_vector.i

%include <crs/CorsikaTypes.h>

%include <crsRead/TCorsikaReader.h>
%include <crsRead/MCorsikaReader.h>;

%include <crs/TSubBlock.h>
%include <crs/MRunHeader.h>
%include <crs/MEventHeader.h>
%include <crs/MEventEnd.h>

%include <crs/TParticleBlockEntry.h>

%include <crs/MLongitudinalBlock.h>

%include <crs/IParticleReadout.h>
%include <crs/MParticle.h>

%template (ParticleCoordsList) std::vector <ParticleCoords>;
%include <custom_accessors.cpp>
