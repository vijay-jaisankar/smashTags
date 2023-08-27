import { Component, OnInit } from '@angular/core';
import { SupportService } from '../support.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-upload-documents',
  templateUrl: './upload-documents.component.html',
  styleUrls: ['./upload-documents.component.scss'],
})
export class UploadDocumentsComponent implements OnInit {
  options = ["Image", "Text", "Audio", "Video"];
  selectedOption = "";
  fileUpload: any;
  textData = "Upload Text";
  constructor(private support: SupportService, private router: Router) { }
  ngOnInit(): void {
    this.options = this.support.getUploadOptions();
    this.selectedOption = this.options[0];
  }

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.fileUpload = file;
      const formData = new FormData();
      formData.append("thumbnail", file);
    }
  }

  goPost(uploadType: string) {
    this.support.uploadFile(uploadType, this.fileUpload);
    // Adding waiting signal
    this.router.navigate(["/post"]);
  }
  postText() {
    this.support.uploadText(this.textData);
    // Adding waiting signal
    this.router.navigate(["/post"]);
  }
}
