// import { empty } from "@apollo/client";

class Anime {
    constructor(id, name, st, sy, eps, dur, gen, tgn, ms, pop, stud, im){
        this.id = id;
        this.name = name;
        this.seasonTime = st;
        this.seasonYear = sy;
        this.numEpisodes = eps;
        this.duration = dur;
        this.genres = gen;
        this.tags = tgn;
        this.meanScore = ms;
        this.popularity = pop;
        this.studios = stud;
        this.img = im;
    }

    changeId(id){
        this.id = id;
    }
    changeName(name){
        this.name = name;
    }
    changeSeasonTime(st){
        this.seasonTime = st;
    }
    changeSeasonYear(sy){
        this.seasonYear = sy;
    }
    changeNumEpisodes(num){
        this.numEpisodes = num;
    }
    changeDuration(dur){
        this.duration = dur;
    }
    changeGenres(gen){
        this.genres = gen;
    }
    changeTags(tgs){
        this.tags = tgs;
    }
    changeMeanScore(ms){
        this.meanScore = ms;
    }
    changePopularity(pop){
        this.popularity = pop;
    }
    changeStudios(stud){
        this.studios = stud;
    }
    changeImg(im){
        this.img = im;
    }

    toString(){
        return this.name.toString();
    }

    toStringExt(){
        return " id:" + this.id + " name:" + this.name + "season:" + this.seasonTime + ":" + this.seasonYear + " eps:" + this.numEpisodes + " duration:" + this.duration + " genres:" + this.genres.join(":") +  " tags:" + this.getTagName() + " ms:" + this.meanScore + " pop:" + this.popularity + " studio" + this.getStudioNames();
        // console.log(this.getStudioNames());
    }

    getTagName(){
        let names = [];
        this.tags.forEach(element => {
            names.push(element.name);
        });
        return names.join(":");
    }
    getStudioNames(){
        let names = [];
        this.studios.forEach(element =>{
            names.push(element.name)
        });
        return names.join(":")
    }
}

export default Anime;