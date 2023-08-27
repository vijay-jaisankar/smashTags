import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class SupportService {
  constructor(private http: HttpClient) { }

  private platforms = [
    { name: "Instagram", icon: "Link", uploads: ["Image"] },
    { name: "Twitter", icon: "Link", uploads: ["Image", "Text"] }
  ]
  private selectedPlatform: string = "";
  private uploadDoc = {
    uploadType: "Image",
    value: "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fhd&psig=AOvVaw2-wldmuATeiyA9QQHLG1jP&ust=1693224217386000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKjI2PLl_IADFQAAAAAdAAAAABAE"
  }

  // Getters and setters start frm here
  getPlatforms() {
    return this.platforms;
  }
  getUploadOptions() {
    for (let plat in this.platforms) {
      if (this.platforms[plat].name == this.selectedPlatform) {
        return this.platforms[plat].uploads;
      }
    }
    let wc = ["Text"];
    return wc;
  }


  setPlatform(pform: string) {
    this.selectedPlatform = pform;
  }

  getHashTags() {
    let url = "http://localhost:5555"
    return this.http.get(url);
  }

  setUploadType(upload: string) {
    this.uploadDoc.uploadType = upload;
  }

  getUploadType() {
    return this.uploadDoc;
  }

}
