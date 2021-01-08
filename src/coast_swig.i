%module coast_wrapper
%{
#include <crsRead/MCorsikaReader.h>
#include <crs/MRunHeader.h>
#include <crs/CorsikaTypes.h>
#include <crs/MEventHeader.h>
%}

%include std_string.i
using std::string;

%include <crs/CorsikaTypes.h>
%include <crsRead/MCorsikaReader.h>
%include <crs/MRunHeader.h>
%include <crs/MEventHeader.h>
