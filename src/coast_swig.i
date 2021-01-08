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

%include <crs/MParticleBlock.h>
typedef std::vector <TParticleBlockEntry> ParticleList;
typedef ParticleList::iterator ParticleListIterator;
typedef ParticleList::const_iterator ParticleListConstIterator;

// class ParticleList {
	
//     public:
//     typedef std::vector <TParticleBlockEntry> ParticleList;
//     typedef ParticleList::iterator ParticleListIterator;
//     typedef ParticleList::const_iterator ParticleListConstIterator;

//     MParticleBlock () {}
//     MParticleBlock (const TSubBlock &right);
//     virtual ~MParticleBlock () {}

//     ParticleListConstIterator FirstParticle () const 
//     {return fParticles.begin ();}
//     ParticleListConstIterator LastParticle () const 
//     {return fParticles.end ();}
//     ParticleList fParticles;
// };

%include <crs/MLongitudinalBlock.h>

%include <crs/IParticleReadout.h>
%include <crs/MParticle.h>
