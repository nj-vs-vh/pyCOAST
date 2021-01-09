// custom functions to 'unwrap' COAST's block classes to plain C sequences


#include <crs/TSubBlock.h>
#include <crs/MParticle.h>
#include <crs/MParticleBlock.h>
#include <crs/TParticleBlockEntry.h>

#include <vector>


struct ParticleCoords {
    crs::ParticleType type;
    float x, y;
};

typedef std::vector <ParticleCoords> ParticleCoordsList;


ParticleCoordsList getParticleCoordsList(crs::TSubBlock * Data) {
    ParticleCoordsList result;

    const crs::MParticleBlock ParticleData = *Data;

    crs::MParticleBlock::ParticleListConstIterator iEntry;
    for (iEntry = ParticleData.FirstParticle(); iEntry != ParticleData.LastParticle(); ++iEntry) {
        if (iEntry->IsParticle()) {
            crs::MParticle particle = *iEntry;
            result.push_back((ParticleCoords){.type = particle.GetType(), .x = particle.GetX(), .y = particle.GetY()});
        }
    }

    return result;
}
