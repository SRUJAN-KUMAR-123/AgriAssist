function settingShow(targetId) {
    detailSection = document.getElementsByClassName("profile-details")[0];
    allDetails = detailSection.querySelectorAll(".detailSection");
    allDetails.forEach(element => {
        element.style.display = 'none';
    });
    detailSection.querySelector('#'+targetId).style.display = 'block';
}