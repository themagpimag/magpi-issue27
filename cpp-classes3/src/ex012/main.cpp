/* W. H. Bell
** A program to demonstrate the usage of operator overloading
*/

#include "TwoVector.h"
#include <iostream>
#include <cmath>

using namespace std;

int main() {

  TwoVector vec1(3.,4.);
  TwoVector vec2 = vec1; // Copy vec1
  std::cout << "vec2{x=" << vec2.x() 
	    << ", y=" << vec2.y() << "}" << std::endl;
  std::cout << "vec1.resultant()=" << vec1.resultant() << std::endl;
  std::cout << "vec2.angle()=" << (vec2.angle()/M_PI)*180. << " degrees" << std::endl;
  vec2.rotate(M_PI/2.0); // Rotate anti-clockwise by 90 degrees
  std::cout << "After rotation vec2{x=" << vec2.x() << ", y=" << vec2.y() 
	    << "}, vec2.angle()=" << (vec2.angle()/M_PI)*180. << " degrees" << std::endl;
  vec1 = vec1 - vec2;
  std::cout << "vec1-vec2 = {x=" << vec1.x() 
	    << ", y=" << vec1.y() << "}" << std::endl;
  return 0;
}
