import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Router } from '@angular/router';
import { HttpHeaders } from '@angular/common/http';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    Authorization: 'my-auth-token',
    // 'Access-Control-Allow-Origin': '*'
  })
};
@Injectable({
  providedIn: 'root'
})
export class SupportService {
  constructor(private http: HttpClient, private router: Router) { }
  private loading: boolean = false;

  private platforms = [
    { name: "Instagram", icon: "http://www.instagram.com", uploads: ["Image", "Video"] },
    { name: "Twitter", icon: "http://www.twitter.com", uploads: ["Image", "Text", "Video"] },
    { name: "Youtube", icon: "http://www.youtube.com", uploads: ["Video"] },
    { name: "Blogger", icon: "http://www.blogger.com", uploads: ["Text"] },
    { name: "Podcast", icon: "http://www.spotify.com", uploads: ["Audio"] }

  ]
  private selectedPlatform: string = "Twitter";
  generatedData = {
    Title: "Sample Title",
    Hashtags: "Sample hashtags"
  };
  results: any;

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

  getGenerateData() {
    return this.generatedData;
  }

  uploadFile(upload: string, uploadFile: File) {
    this.setLoading(true);
    let testData: FormData = new FormData();
    testData.append('image', uploadFile, this.uploadFile.name);
    httpOptions.headers.append('enctype', 'multipart/form-data')
    this.http.post('http://smashtagsapi.pythonanywhere.com/api/' + upload, testData
    ).subscribe((res: any) => {
      this.generatedData.Hashtags = res["hashtags"];
      this.generatedData.Title = res["topic"];
      this.router.navigate(["/post"]);
      this.setLoading(false);
    });

  }
  uploadText(uploadDoc: string) {
    this.setLoading(true);
    let data = {
      "input_text": uploadDoc
    };
    this.http.post("http://smashtagsapi.pythonanywhere.com/api/text/", JSON.stringify(data), httpOptions).subscribe((res: any) => {
      this.generatedData.Title = res["topic"];
      this.generatedData.Hashtags = res["hashtags"];
      this.router.navigate(["/post"]);
      this.setLoading(false);
    });
  }

  setLoading(loading: boolean) {
    this.loading = loading;
  }

  getLoading(): boolean {
    return this.loading;
  }
  getPlatformLink() {
    for (let plat in this.platforms) {
      if (this.platforms[plat].name == this.selectedPlatform) {
        return this.platforms[plat].icon;
      }
    }
    return "None";
  }
}
