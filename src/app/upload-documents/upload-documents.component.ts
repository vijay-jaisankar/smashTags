import { Component, OnInit } from '@angular/core';
import { SupportService } from '../support.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-upload-documents',
  templateUrl: './upload-documents.component.html',
  styleUrls: ['./upload-documents.component.scss'],
})
export class UploadDocumentsComponent implements OnInit {
  options = ["Image", "Text", "Audio"];
  imageFile: any;
  audioFile: any;
  constructor(private support: SupportService, private router: Router) { }
  ngOnInit(): void {
    // this.options = this.support.getUploadOptions();
  }

  onImageSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.imageFile = file;
      const formData = new FormData();
      formData.append("thumbnail", file);
    }
  }
  onAudioSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.audioFile = file;
      const formData = new FormData();
      formData.append("thumbnail", file);
    }
  }


  goPost(uploadType: string) {
    this.support.setUploadType(uploadType);
    this.router.navigate(["/post"]);
  }
}
