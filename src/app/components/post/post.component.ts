import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SupportService } from 'src/app/support.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit {

  constructor(
    private supportService: SupportService,
    private router: Router
  ) { }
  generatedData = {
    Title: "Sample Title",
    Hashtags: "Sample hashtags"
  };
  link = "";

  ngOnInit(): void {
    this.generatedData = this.supportService.getGenerateData();
    this.link = this.supportService.getPlatformLink();
  }
  goBack() {
    this.router.navigate(['upload']);
  }
  postIt() {
    // Call the api to post the document
    this.router.navigate([""]);
  }
}
