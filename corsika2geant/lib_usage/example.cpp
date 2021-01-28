#include <vector>
#include <iostream>

#include "../corsika2geant.hpp"

using namespace std;


int main() {
  vector<ShowerData> sds = LoadShowerDataFromFile("../../data/51PH20DAT000000");

  ShowerData sd = sds[0];

  // just for a test
  cout << "Primary ID = " << sd.metadata.id_primary << endl;
  cout << "Primary E = " << sd.metadata.E_primary << endl;
  cout << "Total number of particles = " << sd.metadata.n_particles << endl;

  cout << endl << "First 10 shower particles:" << endl;
  int particle_count = 0;
  for(vector<ParticleData>::iterator particle = sd.particles.begin(); particle != sd.particles.end(); ++particle) {
    cout << "ID = " << particle->id << ", E = " << particle->E << endl;
    particle_count++;
    if (particle_count > 10) break;
  }

  return 0;
}
