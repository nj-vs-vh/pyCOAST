#include <crsRead/MCorsikaReader.h>

#include <crs/TSubBlock.h>
#include <crs/MRunHeader.h>
#include <crs/MEventHeader.h>
#include <crs/MEventEnd.h>
#include <crs/MParticleBlock.h>
#include <crs/MLongitudinalBlock.h>
#include <crs/MParticle.h>

#include <iostream>
using namespace std;


int main (int argc, char **argv) 
{  
  if (argc<2) {
    cout << "at least one command-line argument is expected (CORSIKA dat file path)" << endl;
    return 1;
  }

  bool verbose;
  string corsikaFilePath;

  if (argc == 2) {
    corsikaFilePath = argv[1];
    verbose = false;
  } else if (argc == 3) {
    string verbosityOpt(argv[1]);
    if (verbosityOpt.compare("-v") == 0) {
      verbose = true;
      corsikaFilePath = argv[2];
    } else {
      cout << "unexpected first command-line argument, expected '-v' or none"<< endl;
      return 1;
    }
  } else {
    cout << "unexpected command-line arguments, expected '<filename>' or '-v <filename>'"<< endl;
    return 1;
  }

  crsRead::MCorsikaReader cr(corsikaFilePath, 3);
  
  int ShowerCounter = 0;
  
  crs::MRunHeader Run;
  while (cr.GetRun (Run)) {
    crs::MEventHeader Shower;
    while (cr.GetShower(Shower)) {
      ++ShowerCounter;

      // Shower data ("header")
      const int ID0 = Shower.GetParticleId();
      const float E0 = Shower.GetEnergy();
      const float theta0 = Shower.GetTheta();
      const float phi0 = Shower.GetPhi();
      cout << "Shower data: " << " ID0 = " << ID0 << "; E0 = " << E0 << "; theta0 = " << theta0 << "; phi0 = " << phi0 << endl;
      
      crs::TSubBlock Data;
      while (cr.GetData (Data)) {
        
        switch (Data.GetBlockType ()) {
          
            case crs::TSubBlock::ePARTDATA:
            {
              const crs::MParticleBlock& ParticleData = Data;

              crs::MParticleBlock::ParticleListConstIterator iEntry;
              for (iEntry = ParticleData.FirstParticle(); iEntry != ParticleData.LastParticle(); ++iEntry) {
                if (iEntry->IsParticle()) {
                  crs::MParticle iPart(*iEntry);
                  
                  // Particle data ("row")
                  const int ID = iPart.GetParticleID();
                  const float x  = iPart.GetX();
                  const float y  = iPart.GetY();
                  const float px = iPart.GetPx();
                  const float py = iPart.GetPy();
                  const float pz = iPart.GetPz();
                  const float E  = iPart.GetKinEnergy();
                  const float t  = iPart.GetTime();
                  
                  if (verbose)  cout << " id: " << ID << " x=" << x << " y=" << y
                                << " px=" << py << " py=" << py << " pz=" << py
                                << " E=" << E << " t=" << t << endl;
                  
                }
              }
              break;
            }
            default:
              break;
        }
        
      }
      
      crs::MEventEnd ShowerSummary;
      cr.GetShowerSummary(ShowerSummary);
      const float Nparticles = ShowerSummary.GetParticles();
      
      cout << "Shower summary: total particles = " << Nparticles << endl << "\n======\n" << endl;
    }
    
  }
  cout << "Read " << ShowerCounter << " showers from file " << endl;
  return 0;
}
