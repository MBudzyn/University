function isPropertyInObject(obj, propName) {
    return obj.hasOwnProperty(propName);
  }
  
  var p = {
    name: 'jan'
  };
  
  var q = {
    surname: 'kowalski'
  };
  
  Object.setPrototypeOf(p, q);
  
  console.log(isPropertyInObject(p, 'name'));    // Zwróci true, ponieważ 'name' jest składową obiektu p.
  console.log(isPropertyInObject(p, 'surname')); // Zwróci false, ponieważ 'surname' jest składową prototypu q.
  
  function listProperties(obj) {
    var ownProperties = [];
    var allProperties = [];
  
    for (var prop in obj) {
      if (isPropertyInObject(obj, prop)) {
        ownProperties.push(prop); // Pola/funkcje występujące tylko w obiekcie
      }
      allProperties.push(prop); // Pola/funkcje występujące w obiekcie i prototypach
    }
  
    return {
      ownProperties: ownProperties,
      allProperties: allProperties
    };
  }
  
  var p = {
    name: 'jan',
    sex: "man"
  };
  
  var q = {
    surname: 'kowalski',
    job: "murarz"
  };
  
  Object.setPrototypeOf(p, q);
  
  var properties = listProperties(p);
  console.log('Pola/funkcje obiektu:', properties.ownProperties);
  console.log('Pola/funkcje obiektu i prototypów:', properties.allProperties);
  