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

}
