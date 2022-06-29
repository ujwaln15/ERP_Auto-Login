//Importing required files
const express = require('express');
const fs = require('fs');
const app=express();

//Starting app on port 3000
app.listen(3000);

//Setting the engine for processing views
app.set('views', __dirname+'/views');
app.set('view engine', 'ejs');

//Requests
app.use(express.static(__dirname+'/public'));
app.use(express.urlencoded({extended:true}));

app.get('/', (req,res)=>{
    res.render('index', {title: "Home", fail: 0});
});

app.get('/create', (req,res)=>{
    res.render('create', {title: "Create"});
});

app.post('/', (req, res)=>{
    res.render('index', {title: "Home", fail: 2});
    const path=__dirname+'/profile.bin';
    const data=Object.values(req.body);
    let file=fs.createWriteStream(path);
    file.on('err', (err)=>{
        console.log(err);
    });
    data.forEach((val)=>{
        file.write(val+'\n');
    });
    file.end();
})

app.get('/activate', (req,res)=>{
    const path=__dirname+'/profile.bin';
    if(fs.existsSync(path)){
        res.render('activate', {title: "Redirecting..."});
        const exec = require("child_process").execFile(__dirname+'/login.exe', [path]);
        exec.stdout.on('data', function(data){
        });
    }
    else{
        res.render('index', {title: "Home", fail: 1});
    }
});

app.post('/activate', (req,res)=>{
    res.redirect('index', {title: "Home", fail: 0});
})

app.use((req,res)=>{
    res.status(404).render('404', {title: "Not Found!"});
});