window.onload = function() {

    // choose something random 
    var id = "L"+Math.floor(20000000*Math.random());
    var worldView = document.getElementById("worldview");
    var inputEntityName = document.getElementById("entityid");
    var inputEntityValue = document.getElementById("value");
    var submit = document.getElementById("submit");
    var debugDom = document.getElementById("debug");

    var host = location.host;

    var myWorld = {};

    function debug( str ) {
        debugDom.innerHTML += " " + str;
    }

    function ajaxReq( obj ) {
        var xhr = new XMLHttpRequest();
        xhr.open( obj["method"] || 'GET', obj["url"]);
        if (obj["content-type"]) {
            xhr.overrideMimeType(obj["content-type"]);
        }
        if (obj["accept"]) {
            xhr.setRequestHeader('Accept', obj["accept"]);
        }
        // This is a call back
        xhr.onreadystatechange = function(){
            // readystate tells you how the transfer is going
            // 4 is done
            if( xhr.readyState === 4 ){
                // This is the HTTP Code
                if(xhr.status === 200){
                    obj["success"]( xhr.responseText );
                } else {
                    alert("There was an error " + xhr.status);
                }
            }
        };
        // finally send it
        xhr.send(obj["body"] || null);
    };
    function jsonReq( obj ) {
        obj["content-type"] = "application/json";
        obj["accept"] = "application/json";
        return ajaxReq( obj );
    }
    // register as a listener
    function register(id) {
        ajaxReq({
            "url":"http://"+host+"/listener/"+id,
            "method":"PUT",
            "body":JSON.stringify({}),
            "success": function(text) {
                // nothing
            }
        });
    }

    // register as a listener
    register(id);
    //
    function checkForUpdate(id) {
        jsonReq({
            "url":"http://"+host+"/listener/"+id,
            "method":"GET",
            "success": function(text) {
                if (text) {
                    var objs = JSON.parse(text);
                    updateWorldWith(objs);
                }
            }
        });
    }

    function modifyWorld(name, value) {
        jsonReq({
            "url":"http://"+host+"/entity/"+name,
            "method":"PUT",
            "body":value,//JSON.stringify(value),
            "success": function(text) {
                // nothing
            }
        });
    }

    function updateWorldWith(objs) {
        for (var key in objs) {
            debug(key);
            myWorld[key] = objs[key];
        }
        drawWorld(myWorld);
    }
    function removeChildren(dom) {
        while( dom.firstChild ) {
            dom.removeChild( dom.firstChild );
        }
    }
    function drawWorld(world) {
        removeChildren( worldView );
        for (var key in world) {
            worldView.appendChild( renderEntity(key, world[key] ) );
        }
    }
    function renderString( str ) {
        var nameSpan = document.createElement("span");
        nameSpan.appendChild( new Text( str ) );
        nameSpan.className = "name";
        return nameSpan;
    }
    function renderEntity(name, value) {
        var dom = document.createElement("div");
        dom.className = "entity";
        dom.appendChild( renderString( name ) );
        dom.appendChild( renderValue( value ) );        
        return dom;
    }
    function renderList( value ) {
        var dom = document.createElement("div");
        dom.className = "list";
        for (var i = 0 ; i  < value.length; i++) {
            dom.appendChild( renderValue(  value[i] ) );
        }
        return dom;
    }
    function renderObject( value ) {
        var dom = document.createElement("div");
        dom.className = "object";
        for (var key in value) {
            dom.appendChild( renderEntity( key,  value[key] ) );
        }
        return dom;
    }
    function renderValue( value ) {
        var t = typeof value;
        if (t === "string") {
            return renderString( value );
        } else if (t === "number") {
            return renderString( value );
        } else if (value instanceof Array) {
            return renderList( value );
        } else if (value instanceof Object) {
            return renderObject( value );
        } else {
            return renderString( "ERROR TYPE "+t);
        }
    }

    // install click listener

    submit.addEventListener("click", function() {
        modifyWorld( inputEntityName.value , inputEntityValue.value );
    });


    setInterval( function() {
        checkForUpdate(id);
    }, 1000);
};
