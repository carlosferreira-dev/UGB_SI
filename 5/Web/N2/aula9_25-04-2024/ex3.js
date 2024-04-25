var skills = ["Javascript", "ReactJS", "React Native"];

function temHabilidade(skills) {
    if (skills.indexOf("Javascript")){
        return true;
    } else {
        return false;
    }
}

alert(temHabilidade(skills));