// custom functions to 'unwrap' COAST's block classes to plain C sequences


#include <crs/TSubBlock.h>
#include <crs/MParticle.h>
#include <crs/MParticleBlock.h>
#include <crs/TParticleBlockEntry.h>

#include <vector>


struct ParticleCoords {
    int id;
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
            if (particle.GetType() == crs::ParticleType::eParticle) {
                result.push_back((ParticleCoords){.id = particle.GetParticleID(), .x = particle.GetX(), .y = particle.GetY()});
            }
        }
    }

    return result;
}
