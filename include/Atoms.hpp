#ifndef _ptens_atoms
#define _ptens_atoms

#include <map>


namespace ptens{

  class Atoms: public vector<int>{
  public:

    map<int,int> lookup;


  public: // ---- Constructors -------------------------------------------------------------------------------


    Atoms(){}

    Atoms(const initializer_list<int>& list){
      for(auto p:list)
	push_back(p);
    }

    Atoms(const vector<int>& x):
      vector<int>(x){
      for(int i=0; i<size(); i++)
	lookup[(*this)[i]]=i;
    }


  public: // ---- Constructors -------------------------------------------------------------------------------


    static Atoms sequential(const int _k){
      vector<int> v(_k);
      for(int i=0; i<_k; i++) v[i]=i;
      return Atoms(v);
    }


  public: // ---- Conversions --------------------------------------------------------------------------------



  public: // ---- Access -------------------------------------------------------------------------------------


    int operator()(const int i) const{
      auto it=lookup.find(i);
      if(it==lookup.end()) return 0;
      return it->second;
    }


    vector<int> operator()(const vector<int>& I) const{
      const int k=I.size();
      vector<int> r(k);
      for(int i=0; i<k; i++)
	r[i]=(*this)(I[i]);
      return r;
    }


    void push_back(const int i){
      lookup[i]=size();
      vector<int>::push_back(i);
    }


    bool includes(const int i) const{
      return lookup.find(i)!=lookup.end();
    }

    
  public: // ---- Operations ---------------------------------------------------------------------------------


    Atoms intersect(const Atoms& y) const{
      Atoms R;
      for(auto p: *this)
	if(y.includes(p)) R.push_back(p);
      return R;
    }


  public: // ---- I/O -----------------------


    string str(const string indent="") const{
      ostringstream oss;
      oss<<"(";
      for(int i=0; i<size()-1; i++)
	oss<<(*this)[i]<<",";
      if(size()>0) oss<<(*this)[size()-1];
      oss<<")";
      return oss.str();
    }


    friend ostream& operator<<(ostream& stream, const Atoms& v){
      stream<<v.str(); return stream;}

  };

}


#endif 