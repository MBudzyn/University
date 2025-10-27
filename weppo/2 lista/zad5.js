
const obiekt1 = {
    pole: "wartość pola",
    metoda: function() {
      console.log("metoda obiektu.");
    },
    _wlasnosc: "wlasnosc",
  
    get wlasnosc() {
      return this._wlasnosc;
    },
  
    set wlasnosc(value) {
      this._wlasnosc = value;
    }
  };
  

  obiekt1.nowePole = "Nowa wartość";
  

  obiekt1.nowaMetoda = function() {
    console.log("nowa metoda");
  };
  
  Object.defineProperty(obiekt1, "nowaWlasnosc", {
    get: function() {
      return this._nowaWlasnosc;
    },
    set: function(value) {
      this._nowaWlasnosc = value;
    }
  });
  
  console.log(obiekt1.pole);
  obiekt1.metoda();
  console.log(obiekt1.wlasnosc);
  
  console.log(obiekt1.nowePole);
  obiekt1.nowaMetoda();
  obiekt1.nowaWlasnosc = "Nowa wartość właściwości";
  console.log(obiekt1.nowaWlasnosc);
